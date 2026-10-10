import { useEffect, useState } from 'react'

const emptyForm = {
  natural_language: 'We need a secure web app for our business with 15 concurrent users, 99.9% uptime, HIPAA-like data sensitivity, and a budget of $5,000 per month.',
  monthly_budget: '$5,000',
  compliance: 'HIPAA, audit logging',
  concurrency: 15,
  region: 'United States',
  workload_type: 'Web application',
}

const emptyAuth = {
  full_name: '',
  email: '',
  password: '',
  company: '',
}

function App() {
  const [form, setForm] = useState(emptyForm)
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [history, setHistory] = useState([])
  const [auth, setAuth] = useState(emptyAuth)
  const [user, setUser] = useState(() => {
    const savedUser = localStorage.getItem('cloud-advisor-user')
    return savedUser ? JSON.parse(savedUser) : null
  })
  const [authMode, setAuthMode] = useState('login')
  const [authOpen, setAuthOpen] = useState(false)
  const [authLoading, setAuthLoading] = useState(false)
  const [saveLoading, setSaveLoading] = useState(false)
  const [exportFormatLoading, setExportFormatLoading] = useState('')
  const [toast, setToast] = useState({ kind: '', message: '' })

  const handleChange = (event) => {
    const { name, value } = event.target
    setForm((prev) => ({ ...prev, [name]: value }))
  }

  const handleAuthChange = (event) => {
    const { name, value } = event.target
    setAuth((prev) => ({ ...prev, [name]: value }))
  }

  const loadHistory = async (email = user?.email || 'guest@example.com') => {
    try {
      const url = `http://localhost:8000/api/recommendations/history?user_email=${encodeURIComponent(email)}`
      const response = await fetch(url)
      const data = await response.json()
      setHistory(data.history || [])
    } catch (error) {
      setHistory([])
    }
  }

  useEffect(() => {
    if (user) {
      localStorage.setItem('cloud-advisor-user', JSON.stringify(user))
    } else {
      localStorage.removeItem('cloud-advisor-user')
    }
  }, [user])

  useEffect(() => {
    loadHistory(user?.email || 'guest@example.com')
  }, [user?.email])

  useEffect(() => {
    if (!toast.message) return

    const timer = window.setTimeout(() => {
      setToast({ kind: '', message: '' })
    }, 3200)

    return () => window.clearTimeout(timer)
  }, [toast])

  const handleSubmit = async (event) => {
    event.preventDefault()
    setLoading(true)

    try {
      const response = await fetch('http://localhost:8000/api/recommendations/build', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          ...form,
          concurrency: Number(form.concurrency || 15),
        }),
      })

      const data = await response.json()
      setResult(data)
      await loadHistory(user?.email || 'guest@example.com')
    } catch (error) {
      setResult({
        error: 'Unable to reach backend. Start the Python API with uvicorn before testing the UI.',
      })
    } finally {
      setLoading(false)
    }
  }

  const handleAuthSubmit = async (event) => {
    event.preventDefault()
    if (authLoading) return

    setAuthLoading(true)
    const endpoint = authMode === 'register' ? '/api/register' : '/api/login'
    const payload = authMode === 'register'
      ? {
          email: auth.email,
          password: auth.password,
          full_name: auth.full_name,
          company: auth.company,
        }
      : {
          email: auth.email,
          password: auth.password,
        }

    try {
      const response = await fetch(`http://localhost:8000${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      })

      const data = await response.json()
      if (!response.ok) {
        throw new Error(data.detail || 'Authentication failed.')
      }

      const nextUser = data.user
      setUser(nextUser)
      setAuthOpen(false)
      setAuth(emptyAuth)
      setToast({
        kind: 'success',
        message: authMode === 'register' ? 'Account created successfully.' : 'Logged in successfully.',
      })
      await loadHistory(nextUser.email)
    } catch (error) {
      setToast({ kind: 'error', message: error.message || 'Authentication failed.' })
    } finally {
      setAuthLoading(false)
    }
  }

  const handleLogout = () => {
    setUser(null)
    setHistory([])
    localStorage.removeItem('cloud-advisor-user')
    setToast({ kind: 'info', message: 'Logged out successfully.' })
  }

  const loadSavedSearch = (item) => {
    if (!item?.payload) return
    setResult(item.payload)
    setToast({ kind: 'info', message: `Loaded saved search: ${item.title || 'Saved recommendation'}` })
  }

  const getUniqueSaveTitle = () => {
    const provider = result?.recommendation?.provider || 'Cloud'
    const workload = form.workload_type || 'workload'
    const stamp = new Date().toISOString().slice(0, 10)
    return `${provider} ${workload} ${stamp}`
  }

  const handleSaveSearch = async () => {
    if (!result || saveLoading) return

    setSaveLoading(true)

    try {
      const response = await fetch('http://localhost:8000/api/recommendations/save', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          user_email: user?.email || 'guest@example.com',
          title: getUniqueSaveTitle(),
          ...result,
        }),
      })
      const data = await response.json()
      if (data.status === 'saved' || data.status === 'mocked') {
        setToast({ kind: 'success', message: 'Recommendation saved successfully.' })
        await loadHistory(user?.email || 'guest@example.com')
      } else {
        setToast({ kind: 'error', message: data.message || 'Unable to save the recommendation history.' })
      }
    } catch (error) {
      setToast({ kind: 'error', message: 'Unable to save the recommendation history.' })
    } finally {
      setSaveLoading(false)
    }
  }

  const handleExport = async (format = 'csv') => {
    if (!result || exportFormatLoading) return

    setExportFormatLoading(format)

    try {
      const response = await fetch(`http://localhost:8000/api/recommendations/export?format=${format}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(result),
      })

      const blob = await response.blob()
      const url = window.URL.createObjectURL(blob)
      const link = document.createElement('a')
      link.href = url
      link.download = `recommendation.${format === 'excel' ? 'xlsx' : format}`
      link.click()
      window.URL.revokeObjectURL(url)
    } catch (error) {
      setToast({ kind: 'error', message: 'Unable to export the recommendation.' })
    } finally {
      setExportFormatLoading('')
    }
  }

  const handleShare = async () => {
    if (!result?.recommendation) return

    const summary = `Cloud Recommendation: ${result.recommendation.provider} - ${result.recommendation.summary}`

    if (navigator.share) {
      try {
        await navigator.share({
          title: 'Cloud recommendation',
          text: summary,
        })
        return
      } catch (error) {
        // fall through to clipboard when share is dismissed
      }
    }

    if (navigator.clipboard) {
      await navigator.clipboard.writeText(summary)
      setToast({ kind: 'success', message: 'Recommendation summary copied to the clipboard.' })
      return
    }

    setToast({ kind: 'info', message: 'Share is not available in this browser, but the summary is ready to copy.' })
  }

  return (
    <div className="app-shell">
      <header className="topbar">
        <div>
          <p className="eyebrow">Cloud advisory platform</p>
          <h1>Cloud Recommendation Engine</h1>
        </div>

        <div className="user-panel">
          {user ? (
            <>
              <span>Signed in as {user.full_name || user.email}</span>
              <button type="button" className="ghost-button" onClick={handleLogout}>Logout</button>
            </>
          ) : (
            <>
              <span>Guest mode</span>
              <button type="button" className="ghost-button" onClick={() => {
                setAuthMode('login')
                setAuthOpen(true)
              }}>
                Login
              </button>
              <button type="button" className="ghost-button" onClick={() => {
                setAuthMode('register')
                setAuthOpen(true)
              }}>
                Register
              </button>
            </>
          )}
        </div>
      </header>

      {toast.message && (
        <div className={`toast ${toast.kind}`}>{toast.message}</div>
      )}

      {!user && (
        <div className="toast info" style={{ marginBottom: '1rem' }}>
          Please log in or register to save recommendations, access your search history, and export saved reports.
        </div>
      )}

      {authOpen && !user && (
        <div className="auth-overlay" onClick={() => setAuthOpen(false)}>
          <div className="panel auth-panel" onClick={(event) => event.stopPropagation()}>
            <div className="auth-header">
              <h2>{authMode === 'register' ? 'Create account' : 'Welcome back'}</h2>
              <button type="button" className="close-button" onClick={() => setAuthOpen(false)}>×</button>
            </div>

            <div className="tab-row">
              <button type="button" className={authMode === 'login' ? 'active' : ''} onClick={() => setAuthMode('login')}>
                Login
              </button>
              <button type="button" className={authMode === 'register' ? 'active' : ''} onClick={() => setAuthMode('register')}>
                Register
              </button>
            </div>

            <p className="auth-hint">Local demo access: demo@example.com / Password123!</p>

            <form onSubmit={handleAuthSubmit} className="form-grid compact">
              {authMode === 'register' && (
                <label>
                  Full name
                  <input name="full_name" value={auth.full_name} onChange={handleAuthChange} />
                </label>
              )}

              <label>
                Email
                <input name="email" value={auth.email} onChange={handleAuthChange} />
              </label>

              <label>
                Password
                <input type="password" name="password" value={auth.password} onChange={handleAuthChange} />
              </label>

              {authMode === 'register' && (
                <label>
                  Company
                  <input name="company" value={auth.company} onChange={handleAuthChange} />
                </label>
              )}

              <button type="submit" disabled={authLoading}>
                {authLoading ? (authMode === 'register' ? 'Creating account...' : 'Logging in...') : (authMode === 'register' ? 'Create account' : 'Login')}
              </button>
            </form>
          </div>
        </div>
      )}

      <main className="layout">
        <section className="panel requirements-panel">
          <h2>Requirements</h2>
          <form onSubmit={handleSubmit} className="form-grid requirements-form">
            <label>
              Requirement summary
              <textarea
                name="natural_language"
                rows="6"
                value={form.natural_language}
                onChange={handleChange}
              />
            </label>

            <div className="two-column">
              <label>
                Monthly budget
                <input name="monthly_budget" value={form.monthly_budget} onChange={handleChange} />
              </label>
              <label>
                Concurrency
                <input name="concurrency" type="number" value={form.concurrency} onChange={handleChange} />
              </label>
            </div>

            <div className="two-column">
              <label>
                Compliance
                <input name="compliance" value={form.compliance} onChange={handleChange} />
              </label>
              <label>
                Region
                <input name="region" value={form.region} onChange={handleChange} />
              </label>
            </div>

            <label>
              Workload type
              <input name="workload_type" value={form.workload_type} onChange={handleChange} />
            </label>

            <button type="submit" disabled={loading}>
              {loading ? 'Analyzing...' : 'Generate Recommendation'}
            </button>
          </form>
        </section>

        <section className="panel results-panel">
          <h2>Results</h2>

          {!result && <p className="empty-state">No recommendation generated yet.</p>}

          {result?.error && <p className="error">{result.error}</p>}

          {result?.recommendation && (
            <div className="results">
              <div className="score-box">
                <span>Best fit</span>
                <strong>{result.recommendation.provider}</strong>
                <em>Fit score: {result.recommendation.fit_score}/100</em>
              </div>

              <h3>Architecture</h3>
              <p>{result.recommendation.architecture}</p>

              <h3>Recommended services</h3>
              <ul>
                {result.recommendation.services.map((service) => (
                  <li key={service}>{service}</li>
                ))}
              </ul>

              <h3>Service-level price breakdown</h3>
              {result.recommendation.service_level_breakdown && (
                <table>
                  <thead>
                    <tr>
                      <th>Service</th>
                      <th>Provider</th>
                      <th>Monthly estimate</th>
                    </tr>
                  </thead>
                  <tbody>
                    {result.recommendation.service_level_breakdown.map((item) => (
                      <tr key={`${item.service}-${item.provider}`}>
                        <td>{item.service}</td>
                        <td>{item.provider}</td>
                        <td>{item.monthly_estimate}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )}

              <h3>Similar services comparison</h3>
              {result.recommendation.similar_services && (
                <table>
                  <thead>
                    <tr>
                      <th>Service</th>
                      <th>Provider</th>
                      <th>Monthly estimate</th>
                    </tr>
                  </thead>
                  <tbody>
                    {result.recommendation.similar_services.map((item) => (
                      <tr key={`${item.service}-${item.provider}`}>
                        <td>{item.service}</td>
                        <td>{item.provider}</td>
                        <td>{item.monthly_estimate}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )}

              <h3>Monthly cost estimate</h3>
              <table>
                <thead>
                  <tr>
                    <th>Provider</th>
                    <th>Estimate</th>
                  </tr>
                </thead>
                <tbody>
                  {Object.entries(result.recommendation.cost_estimate.comparison).map(([provider, value]) => (
                    <tr key={provider}>
                      <td>{provider}</td>
                      <td>{value}</td>
                    </tr>
                  ))}
                </tbody>
              </table>

              <h3>Trade-offs</h3>
              <ul>
                {result.recommendation.tradeoffs.map((tradeoff) => (
                  <li key={tradeoff}>{tradeoff}</li>
                ))}
              </ul>

              <h3>Summary</h3>
              <p>{result.recommendation.summary}</p>

              <div className="action-row">
                <button type="button" onClick={handleSaveSearch} disabled={saveLoading}>
                  {saveLoading ? 'Saving...' : 'Save search'}
                </button>
                <button type="button" onClick={() => handleExport('csv')} disabled={!!exportFormatLoading}>
                  {exportFormatLoading === 'csv' ? 'Exporting CSV...' : 'Export CSV'}
                </button>
                <button type="button" onClick={() => handleExport('excel')} disabled={!!exportFormatLoading}>
                  {exportFormatLoading === 'excel' ? 'Exporting Excel...' : 'Export Excel'}
                </button>
                <button type="button" onClick={() => handleExport('html')} disabled={!!exportFormatLoading}>
                  {exportFormatLoading === 'html' ? 'Preparing HTML...' : 'Export HTML'}
                </button>
                <button type="button" onClick={() => handleExport('pdf')} disabled={!!exportFormatLoading}>
                  {exportFormatLoading === 'pdf' ? 'Exporting PDF...' : 'Export PDF'}
                </button>
                <button type="button" onClick={handleShare}>Share</button>
              </div>
            </div>
          )}
        </section>

        <section className="panel history-panel">
          <h2>Search history</h2>
          {!user ? (
            <p className="empty-state">Login or register to view your saved searches and recommendation history.</p>
          ) : history.length === 0 ? (
            <p className="empty-state">No saved searches yet for this account.</p>
          ) : (
            <ul className="history-list">
              {history.map((item) => (
                <li
                  key={item.id || item.title}
                  onDoubleClick={() => loadSavedSearch(item)}
                  onClick={() => loadSavedSearch(item)}
                  role="button"
                  tabIndex={0}
                  onKeyDown={(event) => {
                    if (event.key === 'Enter' || event.key === ' ') {
                      event.preventDefault()
                      loadSavedSearch(item)
                    }
                  }}
                >
                  <strong>{item.title || 'Saved search'}</strong>
                  <span>{item.status || 'saved'}</span>
                </li>
              ))}
            </ul>
          )}
        </section>
      </main>
    </div>
  )
}

export default App
