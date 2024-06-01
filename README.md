
# **Codestract** — Codebase Context Extraction for LLMs

<br>

<div align="center">
  <img src="readme-image.gif" alt="codestract-main" width="1280"/>
</div>
<br>


Codestract is a powerful command-line tool designed to extract and consolidate text-based files from your codebase into a single context file. This tool is particularly useful for developers working with Large Language Models (LLMs), as it allows them to efficiently prepare their codebase for analysis or fine-tuning.

## Features

- **Recursive Directory Traversal**: Codestract traverses through all subdirectories within a specified directory, ensuring that no file is left behind.
- **File Exclusion**: Supports exclusion of files based on extension, such as image files and others, customizable to include additional file types.
- **Timestamp-based Output Files**: Generates a new output file with a timestamp each time the script is run, saved in a specified output directory.
- **Project Structure Summary**: Provides a summary of the project structure, including a count of processed and skipped files and directories.
- **Encoding Support**: Supports various file encodings, which helps in reading a wide range of text-based files.

## Requirements

- **Python**: Python 3.8+ is required to run the script.

## Installation

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/arnovandash/codestract-context-tool.git
cd codestract-context-tool
```

## Usage

To use the script, execute it from your terminal. It will start the process of scanning for files and appending their contents to the specified output file.

```bash
python3 main.py <directory_path>
```
Ensure to replace `<directory_path>` with the path of the directory you want to process.


## Ignoring Files and Directories

Create a `.ignore` file in the `.codestract` directory to specify files and directories to exclude. List the names of files to be ignored on separate lines. To exclude an entire directory, postfix its name with a `/`.

Example `.ignore` file:

```bash
# Exclude files
secrets.txt
config.json

# Exclude directories
logs/
tests/
```

## Roadmap

Future improvements include:
- **GUI Implementation**: To enhance user interaction and provide a more user-friendly experience.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
