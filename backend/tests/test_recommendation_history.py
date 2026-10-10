import unittest
import uuid
from io import BytesIO
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient
from openpyxl import load_workbook

from app.main import app
from app.services.auth_service import AuthService
from app.services.database_service import DatabaseService
from app.services.export_service import ExportService


class RecommendationHistoryTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_save_endpoint_keeps_only_recommendation_payload(self):
        response = self.client.post(
            "/api/recommendations/save",
            json={
                "user_email": "demo@example.com",
                "title": "API Save Test",
                "prompt": "Need a secure web app",
                "recommendation": {"provider": "Azure", "summary": "Managed app services"},
                "ai_status": {"status": "ok"},
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "saved")

        history_response = self.client.get(
            "/api/recommendations/history",
            params={"user_email": "demo@example.com"},
        )

        self.assertEqual(history_response.status_code, 200)
        history = history_response.json()["history"]
        self.assertTrue(history)
        self.assertEqual(history[0]["title"], "API Save Test")
        payload = history[0]["payload"]
        self.assertEqual(payload["recommendation"]["provider"], "Azure")
        self.assertNotIn("user_email", payload)
        self.assertNotIn("title", payload)


class AuthUserPersistenceTests(unittest.TestCase):
    def test_registered_user_is_persisted_and_can_authenticate(self):
        email = f"persisted_{uuid.uuid4().hex[:8]}@example.com"
        password = "StrongPass!123"

        AuthService.register_user(email, password, "Persisted User", "Example Co")

        conn = DatabaseService.get_connection()
        self.assertIsNotNone(conn)
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT email, password_hash FROM users WHERE email = %s", (email,))
                row = cur.fetchone()
                self.assertIsNotNone(row)
                self.assertEqual(row[0], email)
        finally:
            conn.close()

        auth = AuthService.authenticate_user(email, password)
        self.assertIsNotNone(auth)
        self.assertEqual(auth["email"], email)


class ExportTests(unittest.TestCase):
    def test_export_formats_are_tabular_and_html_report_is_available(self):
        data = {
            "recommendation": {
                "provider": "Azure",
                "fit_score": 92,
                "architecture": "App Service + PostgreSQL",
                "services": ["App Service", "Azure Database for PostgreSQL"],
                "summary": "Best fit for this workload.",
                "service_level_breakdown": [
                    {"service": "App Service", "provider": "Azure", "monthly_estimate": "$120"},
                    {"service": "PostgreSQL", "provider": "Azure", "monthly_estimate": "$95"},
                ],
                "similar_services": [
                    {"service": "EC2 + RDS", "provider": "AWS", "monthly_estimate": "$150"},
                    {"service": "Cloud SQL", "provider": "GCP", "monthly_estimate": "$140"},
                ],
                "cost_estimate": {"comparison": {"AWS": "$180", "Azure": "$215", "GCP": "$205"}},
            }
        }

        csv_content = ExportService.to_csv(data)
        self.assertIn("Service,Provider,Monthly estimate", csv_content)
        self.assertIn("App Service,Azure,$120", csv_content)
        self.assertNotIn("Best fit for this workload.", csv_content)

        excel_bytes = ExportService.to_excel_bytes(data)
        self.assertTrue(excel_bytes)
        workbook = load_workbook(BytesIO(excel_bytes), data_only=True)
        self.assertEqual(workbook["Service breakdown"]["C2"].value, "$120")

        html = ExportService.to_html_report(data)
        self.assertIn("<html", html.lower())
        self.assertIn("<details", html.lower())
        self.assertIn("App Service", html)
        self.assertIn("Azure", html)
        self.assertIn("$120", html)

    def test_pdf_export_returns_a_valid_document(self):
        pdf_bytes = ExportService.to_pdf_bytes({
            "recommendation": {
                "provider": "Azure",
                "fit_score": 92,
                "architecture": "App Service with PostgreSQL",
                "summary": "Recommended for managed services and compliance controls.",
                "service_level_breakdown": [
                    {"service": "App Service", "provider": "Azure", "monthly_estimate": "$120"},
                ],
                "cost_estimate": {"monthly_estimate": "$120"},
            },
        })

        self.assertTrue(pdf_bytes.startswith(b"%PDF"))
        self.assertGreater(len(pdf_bytes), 1000)

    def test_export_endpoint_returns_downloads_for_supported_formats(self):
        client = TestClient(app)
        payload = {
            "recommendation": {
                "provider": "Azure",
                "fit_score": 92,
                "architecture": "App Service with PostgreSQL",
                "summary": "Managed services meet the stated requirements.",
                "service_level_breakdown": [
                    {"service": "App Service", "provider": "Azure", "monthly_estimate": "$120"},
                ],
                "cost_estimate": {"monthly_estimate": "$120"},
            },
        }
        exports = {
            "csv": ("text/csv", "recommendation.csv"),
            "excel": (
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                "recommendation.xlsx",
            ),
            "html": ("text/html", "recommendation.html"),
            "pdf": ("application/pdf", "recommendation.pdf"),
        }

        with self.assertLogs("app.routers.recommendations", level="INFO") as captured_logs:
            for export_format, (media_type, filename) in exports.items():
                with self.subTest(format=export_format):
                    response = client.post(
                        "/api/recommendations/export",
                        params={"format": export_format},
                        json=payload,
                    )

                    self.assertEqual(response.status_code, 200)
                    self.assertTrue(response.headers["content-type"].startswith(media_type))
                    self.assertIn(filename, response.headers["content-disposition"])
                    self.assertTrue(response.content)

        self.assertTrue(any("Recommendation export generated" in entry for entry in captured_logs.output))

    def test_export_endpoint_logs_and_propagates_generation_errors(self):
        client = TestClient(app)

        with patch(
            "app.routers.recommendations.ExportService.export",
            side_effect=ValueError("unsupported payload"),
        ):
            with self.assertLogs("app.routers.recommendations", level="ERROR") as captured_logs:
                with self.assertRaises(ValueError):
                    client.post(
                        "/api/recommendations/export",
                        params={"format": "pdf"},
                        json={"recommendation": {}},
                    )

        self.assertIn("Recommendation export failed", captured_logs.output[0])


class AuthDefaultsTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_frontend_auth_form_starts_empty_for_new_users(self):
        frontend_source = Path(__file__).resolve().parents[2] / "frontend" / "src" / "App.jsx"
        source = frontend_source.read_text(encoding="utf-8")

        self.assertIn("const emptyAuth = {", source)
        self.assertIn("full_name: '',", source)
        self.assertIn("email: '',", source)
        self.assertIn("password: '',", source)
        self.assertNotIn("email: 'demo@example.com'", source)
        self.assertNotIn("password: 'Password123!'", source)

    def test_recommendation_contains_service_breakdown_and_similar_services(self):
        response = self.client.post(
            "/api/recommendations/build",
            json={
                "natural_language": "We need a secure healthcare web app with HIPAA, API and PostgreSQL database.",
                "monthly_budget": "$8000",
                "compliance": "HIPAA, audit logging",
                "concurrency": 500,
                "region": "United States",
                "workload_type": "Web application",
            },
        )

        self.assertEqual(response.status_code, 200)
        recommendation = response.json()["recommendation"]
        self.assertIn("service_level_breakdown", recommendation)
        self.assertIn("similar_services", recommendation)
        self.assertTrue(recommendation["service_level_breakdown"])
        self.assertTrue(recommendation["similar_services"])


if __name__ == "__main__":
    unittest.main()
