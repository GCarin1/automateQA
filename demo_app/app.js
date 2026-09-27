// Demo SUT logic: a fake login kept in sessionStorage. Not a real auth system.
const DEMO_USER = { name: "demo", password: "demo-password" };
const SESSION_KEY = "demo-app-user";

function initLoginPage(form) {
  const error = form.querySelector('[data-testid="login-error"]');
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const name = form.username.value.trim();
    const password = form.password.value;
    if (!name || !password) {
      showError(error, "Username and password are required.");
      return;
    }
    if (name !== DEMO_USER.name || password !== DEMO_USER.password) {
      showError(error, "Invalid username or password.");
      return;
    }
    sessionStorage.setItem(SESSION_KEY, name);
    window.location.assign("home.html");
  });
}

function initHomePage(welcome) {
  const user = sessionStorage.getItem(SESSION_KEY);
  if (!user) {
    window.location.replace("index.html");
    return;
  }
  welcome.textContent = `Welcome, ${user}!`;
  document.querySelector('[data-testid="logout-button"]').addEventListener("click", () => {
    sessionStorage.removeItem(SESSION_KEY);
    window.location.assign("index.html");
  });
}

function showError(element, message) {
  element.textContent = message;
  element.hidden = false;
}

const loginForm = document.querySelector('[data-testid="login-form"]');
const welcomeMessage = document.querySelector('[data-testid="welcome-message"]');
if (loginForm) initLoginPage(loginForm);
if (welcomeMessage) initHomePage(welcomeMessage);
