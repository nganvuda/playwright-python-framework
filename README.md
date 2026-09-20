# Playwright Python Test Automation Framework

A Page Object Model (POM) test automation framework built with **Playwright** and **pytest**, testing the end-to-end purchase flow of [practicesoftwaretesting.com](https://practicesoftwaretesting.com), a public demo e-commerce site.

Built as a learning project and portfolio piece to demonstrate practical QA automation skills: page object design, component reuse, environment configuration, structured test data, and debugging real flaky-test scenarios encountered along the way.

## What it tests

- **Login** — valid and invalid credentials
- **Product search & selection** — searching the catalog and navigating to a product page
- **Add to cart** — verifying cart count updates correctly
- **Full checkout flow** — cart → sign in → billing address → payment → order confirmation

## Tech stack

- [Playwright](https://playwright.dev/python/) (sync API) — browser automation
- [pytest](https://docs.pytest.org/) + [pytest-playwright](https://github.com/microsoft/playwright-pytest) — test runner and fixtures
- `python-dotenv` — environment/secret management

## Architecture

```
├── pages/              # Page Object classes (one per page)
│   ├── base_page.py    # Shared behavior for every page (title, refresh, header)
│   ├── home_page.py
│   ├── login_page.py
│   ├── product_page.py
│   └── checkout_page.py
├── components/         # Reusable UI components shared across pages
│   ├── header_component.py       # Nav bar: sign-in, account menu, cart
│   └── login_form_component.py   # Login form (reused on LoginPage and CheckoutPage)
├── utils/
│   ├── config.py        # Environment-driven config (BASE_URL, credentials)
│   └── logger.py         # Logging setup
├── tests/                # Test files
├── test_data.py          # Structured test data (User, Address dataclasses)
├── conftest.py            # Shared pytest fixtures
└── pytest.ini              # Pytest config: screenshots/video/trace on failure, markers
```

**Design choices worth noting:**
- **Page Object Model** with a `BasePage` parent class, so shared elements (like the header) are available on every page without duplication.
- **Component objects** for UI pieces reused across multiple pages (e.g. the login form appears both on the standalone login page and embedded inside checkout — one class, two usages).
- **Structured test data** via Python dataclasses (`User`, `Address`) rather than loose constants, for readability and IDE autocomplete/typo-catching.
- **Fixtures for shared setup** — e.g. a `checkout_at_billing_address` fixture handles the common cart → sign-in → billing-address path so individual tests stay focused on what they're actually verifying.

## Setup

**Prerequisites:** Python 3.10+ and Git.

```bash
git clone https://github.com/nganvuda/playwright-python-framework.git
cd playwright-python-framework

python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

pip install -r requirements.txt
playwright install
```

**Environment variables:** copy `.env.example` to `.env` and fill in real values:
```bash
cp .env.example .env
```
```
TEST_EMAIL=your_test_account_email
TEST_PASSWORD=your_test_account_password
```

## Running tests

```bash
pytest                                    # run everything
pytest tests/test_product.py -s           # run one file, show logs live
pytest -m smoke                           # run only smoke-marked tests
```

On failure, a screenshot, video, and full [Playwright trace](https://playwright.dev/python/docs/trace-viewer-intro) are automatically saved under `test-results/`:
```bash
playwright show-trace test-results/<folder>/trace.zip
```

## A few things I debugged along the way

Building this surfaced some real, non-obvious issues worth mentioning:
- **A network race condition** on the home page — a slow initial catalog request could silently overwrite correct search results if it resolved after the search request. Fixed by waiting for the DOM to settle before interacting with the page.
- **A whitespace/matching bug** — a raw regex locator (`re.compile(f"^{name}$")`) doesn't normalize whitespace the way Playwright's native `:text-is()` selector does, causing a locator that worked in the Inspector to silently match zero elements in code.
- **Cross-platform portability** — migrating the project to a second machine (Windows → macOS) surfaced a Python-version dependency conflict and an over-strict `networkidle` wait that never resolved on this particular site.

## CI status

GitHub Actions is configured and runs the full suite on every push (see
`.github/workflows/tests.yml`). Locally, and from most networks, all tests pass.

**Known limitation:** the target site (practicesoftwaretesting.com) uses
Cloudflare bot-protection that blocks traffic from GitHub-hosted runners'
IP ranges, showing a "Verify you are human" challenge instead of the real
page. This is expected — it's the same protection a real user would see if
flagged as suspicious traffic, not a bug in the framework. Confirmed via
the failure screenshots captured by the workflow's trace/artifact upload.

## Roadmap

- [ ] API + UI combined tests
- [ ] Parallel test execution
- [ ] CI pipeline (GitHub Actions)
- [ ] Dockerized test environment
