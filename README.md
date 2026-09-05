# Pydantic Models

Week 1 practice project of my AI Engineer learning/practice roadmap: data contracts with Pydantic, tests, and professional tooling.

## Content

**User** - Model with simple validation for a valid email address.

**Product** - Price validation using `field_validator` to ensure that the price is greater than zero.
Also rounds decimal values to 2 decimal places.

**Order** - Model that contains a list of valid products, with a property field that calculates the total price by applying a discount based on the product price.

**Ticket** - Model that contains ticket information, with a catalog of statuses.

**Reservation** - Model that contains reservation information with a `model_validator` that validates that the end date is later than the reservation start date.

## Usage

**uv** - uv must be installed and run uv sync

**test** - Runs the tests defined for the models using pytest.

**lint** - Uses Ruff to first format the code and then perform syntax checking.

**run** - Opens an interactive Python REPL with all models pre-imported.

## Learning

- I understood the difference between `assert` and `with pytest.raises`, since `assert` validates the exact output of a model, while `pytest.raises` succeeds when an error has been intentionally and properly captured. **Related lesson:** A test only protects what it executes, ensure your tests cover the most critical scenarios like Defaults and validators.

- It is important not to omit `return` statements at the end of functions, as well as to use `self` as the return value when implementing a `model_validator`.

- Correctly using the unified assignment and operation with the `+=` operator is important, since placing the operators in the wrong order produces a different result. `+=` accumulate, `=+` reassigns.

- Building `Producto(...)` validates piece by piece but loses the error path; passing dicts lets `Orden` validate in cascade and pinpoint the exact location (`productos.1.precio`). Same result with valid data, so I prefer dicts: external data always arrives as JSON/keys.

- I learned that a task should not be considered "Done" until the commit has been pushed, then through a Pull Request into a development branch, and finally merged into `main`.