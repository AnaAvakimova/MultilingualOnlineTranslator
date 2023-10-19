# Multilingual Online Translator

## Description
This script is a command-line tool that allows users to translate words between multiple languages by scraping data from an online source. It offers the capability to translate a word into one specific language or all supported languages.
This project was created for educational purposes based on https://hyperskill.org/ course.

## Features
* Translate words into one of several supported languages.
* Translate words into all supported languages simultaneously.
* Custom exceptions handling for unsupported languages or words that cannot be translated.

## Supported Languages

The script supports translations between the following languages:

* Arabic
* German
* English
* Spanish
* French
* Hebrew
* Japanese
* Dutch
* Polish
* Portuguese
* Romanian
* Russian
* Turkish

## Installation
To use the tool, follow these steps:
1. Clone this repository to your local machine.
2. Open a terminal (Command Prompt, PowerShell, or any other terminal you use).
3. Navigate to the directory where the script is located.
5. Run the script using Python with the required arguments:
```sh
python translator.py <source_language> <target_language> <word>
```
Replace <source_language> with the language you are translating from, <target_language> with the language you are translating into (or 'all' to translate into all supported languages), and <word> with the word you want to translate.

Example:
```sh 
python translator.py english spanish hello
```
This command would translate the word "hello" from English to Spanish.

The translations will be saved in a text file named <word>.txt in the current directory and printed to the console.

## Error Handling
The script includes error handling for situations where the input language is not supported or the word cannot be found for translation. In these cases, user-friendly error messages will be displayed in the console.
