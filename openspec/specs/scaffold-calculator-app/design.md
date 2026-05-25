# Design Specification: Glassmorphic Calculator

## Architectural Overview
A decoupled client-server architecture. The frontend issues asynchronous `fetch` API commands containing JSON structures to a stateless Flask microservice.

## Backend Architecture (Python / Flask)
### Endpoints
- `GET /`: Serves the static presentation entry point `templates/index.html`.
- `POST /calculate`: Processes arithmetic operations.
  - **Payload Structure:**
    ```json
    {
      "num1": 10.5,
      "num2": 5.0,
      "operation": "add"
    }
    ```
  - **Supported Operations:** `add`, `subtract`, `multiply`, `divide`.
  - **Error States:** Gracefully returns `400 Bad Request` with an explicit JSON payload `{ "error": "Cannot divide by zero" }` or invalid characters to block edge-case crashes.

## Frontend Architecture (HTML5 / CSS3 / JavaScript)
- **UI Styling Elements:**
  - Base: Cosmic Deep Space Dark (`#0a0b10`) with vibrant neon background glow maps.
  - Frost Layer: Modern frosted-glass aesthetic applied via CSS `backdrop-filter: blur(20px)`.
  - Typography: Premium typography using google-loaded 'Outfit' / 'Inter' fonts.
- **State Management:**
  - Expression building handled inside a local UI text buffer.
  - Historical entries persisted sequentially within browser `localStorage` to feed the slide-out history panel drawer.
- **Accessibility (a11y):**
  - Structural landmark markup using semantic HTML5 tags.
  - Sequential keyboard accessibility using strict `:focus-visible` ring tracking layouts.