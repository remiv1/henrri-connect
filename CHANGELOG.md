# Changelog for henrri-connect

## [0.1.0] - 2026-06

### Added

- Initial release of henrri-connect, a Python SDK for integrating with Henrri billing services.
- Basic structure and setup for the SDK, including installation instructions and placeholder for usage documentation.
- Publication instructions for building and uploading the package to PyPI.
- Documentation update instructions for generating and copying HTML documentation to the appropriate directory.
- README.md file with an introduction to the library, installation instructions, and a placeholder for usage examples.
- CHANGELOG.md file to track changes and updates to the library.
- .gitignore file to exclude unnecessary files from version control.
- setup.py file for packaging and distribution of the library.
- LICENSE file to specify the licensing terms for the library.
- requirements.txt file to list dependencies for the library.
- tests/ directory with placeholder for unit tests.
- documentation/ directory with Sphinx documentation setup.
- .git/ directory for version control with Git.

## [0.1.1] - 2026-06-01

### Added 0.1.1

- Make complete documentation in the README.md file, with sections for each sub-client (customers, documents, document_lines, document_line_types, document_types, users, secures).
- Add examples for both synchronous and asynchronous usage for each sub-client.
- Update the changelog to reflect the new version and the added documentation.

## [0.1.2] - 2026-06-02

### Added 0.1.2

- Add a disclaimer in the README.md file to clarify that this SDK is an unofficial client for the Henrri API and is not affiliated, supported, or endorsed by Henrri. Include a note about Henrri being a registered trademark of its publisher.
- Add a logger into the connect client to allow users to enable logging of API requests and responses for debugging purposes.
- Add a logo image to the README.md file for better visual appeal and branding of the henrri-connect library.
- Update the changelog to reflect the new version and the added disclaimer and logo in the README.md file.

## [0.1.3] - 2026-06-01

### Fixed 0.1.3

- Fix a bug in the asynchronous client where the wrong method was being called for listing items. Update the example code in the README.md file to use the correct method for listing items in asynchronous mode.
- Update the changelog to reflect the new version and the fixed bug in the asynchronous client example in the README.md file.
- Update the README.md file to use ``await main()`` instead of ``asyncio.run(main())`` for running the asynchronous example, to better align with modern async practices in Python.
- Update the README.md file to include a type cast for the asynchronous client to avoid type errors in IDEs when using the async mode of the HenrriClient.

## [0.1.4] - 2026-06-02

### Fixed 0.1.4

- Fix type/stub issues in the asynchronous/synchronous client by adding proper type annotations and ensuring that the async/sync client is correctly initialized and used in the example code in the README.md file.

## [0.1.5] - 2026-06-03

### Added 0.1.5

- Delete the ``async_mode`` parameter from the Client and separate the synchronous and asynchronous clients into ``SyncHenrriClient`` and ``AsyncHenrriClient`` respectively, to provide clearer and more explicit client classes for users. Update the example code in the README.md file to reflect this change and show how to use both the synchronous and asynchronous clients correctly.
- Add a MANIFEST.in file to include stub files and py.typed files in the source distribution, ensuring that type information is included when the package is distributed.

## [0.1.6] - 2026-06-04

### Documentation 0.1.6

- Create a complete documentation for each module, Object Class, Pydantics Models, function or methodes of this package.
  
### Added 0.1.6

- Refactor code to expose necessaries models for each class in modules.

## [0.2.0] - 2026-06-05

### Documentation 0.2.0

- Better readness for documentation with cutted documentation in trees for navigation between modules.