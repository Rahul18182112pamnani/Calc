# Changelog

## [1.9.0] - 2024-11-07
### Fixed

- Resolved issues with continuous calculations: new inputs after an operation now start fresh instead of modifying the previous result.
- Corrected backspace behavior to ensure it works as expected without corrupting calculations.
- Addressed edge cases for clear and reset operations: calculations after using the clear button now work correctly.
- Fixed decimal precision issues to prevent floating-point errors (e.g., 0.1 * 0.2 now correctly outputs 0.02).

## [1.8.0] - 2024-10-14
### Fixed
- Resolved issues with multiple operations not working correctly after clearing.
- Fixed `=` button behavior for repeated calculations.
- Improved handling of decimal inputs (e.g., `.1` treated as `0.1`).

## [1.7.0] - 2024-09-27
### Changed
- Optimized for better error handling across all test cases.

## [1.6.0] - 2024-09-26
### Fixed
- Ensured consistent button styling.
- Resolved keyboard input errors.
- Fixed various corner cases and unexpected outputs.

## [1.5.0] - 2024-09-17
### Changed
- Improved UI design to mimic Windows Calculator.
- Adjusted window size to 450x750.

## [1.4.0] - 2024-09-14
### Added
- Keyboard integration for better user experience.

## [1.3.0] - 2024-09-10
### Fixed
- Corrected error handling for invalid inputs and operations (e.g., division by zero).
- Resolved issues with backspace and clear functionalities.

## [1.2.0] - 2024-09-07
### Changed
- Improved user interface with better styling and formatting.
- Memory functions added (Memory Add, Memory Subtract, Memory Clear, Memory Recall).

## [1.1.0] - 2024-09-05
### Added
- Additional functionalities: square, cube, and change of positive/negative sign.

## [1.0.0] - 2024-09-01
### Added
- Initial version of the basic calculator with basic operations (addition, subtraction, multiplication, division).
