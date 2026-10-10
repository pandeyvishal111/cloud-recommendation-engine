from __future__ import annotations

from azure.storage.blob import BlobClient, BlobServiceClient

from app.config import settings


class BlobStorageService:
    def __init__(self):
        self.connection_string = settings.AZURE_STORAGE_CONNECTION_STRING
        self.service_client = BlobServiceClient.from_connection_string(self.connection_string)

    def upload_bytes(self, file_name: str, content: bytes, container: str = "recommendations") -> dict:
        try:
            container_client = self.service_client.get_container_client(container)
            container_client.create_container(exist_ok=True)
            blob_client = BlobClient.from_connection_string(
                conn_str=self.connection_string,
                container_name=container,
                blob_name=file_name,
            )
            blob_client.upload_blob(content, overwrite=True)
            return {
                "status": "uploaded",
                "container": container,
                "file_name": file_name,
                "url": blob_client.url,
            }
        except Exception as exc:
            return {
                "status": "error",
                "message": str(exc),
                "container": container,
                "file_name": file_name,
            }

    def list_files(self, container: str = "recommendations") -> list[str]:
        try:
            container_client = self.service_client.get_container_client(container)
            return [blob.name for blob in container_client.list_blobs()]
        except Exception as exc:
            return [{"status": "error", "message": str(exc)}]
