# <p align="center">Loggefy: Simple Log and Notify</p>

Loggefy is a versatile logging utility designed to simplify the process of generating and managing logs within your projects. This Python module offers an intuitive interface for recording various types of messages, including informative, warning, and error messages. With an optional notification feature, Loggefy keeps you informed about important events in your application.

### Key Features:

- **Flexible Logging**: Loggefy provides a user-friendly API for logging messages to a file, making it easy to keep track of important events in your application.

- **Notification Integration**: Receive real-time notifications for critical events directly on your desktop. This feature is especially useful for staying updated on important developments in your project.

- **Customizable Icons**: Personalize your notifications by setting custom icons to differentiate between various types of messages.

- **Subtitle Support**: Loggefy allows you to categorize messages under different subtitles, providing an organized view of your logs.

- **Clear Console Output**: Enable console output for a clean and clear view of log messages during development.

- **Error Handling**: Loggefy offers detailed error messages, making it easy to identify and address issues in your application.

### Usage:

```python
#   Set the Log folder
Log.path = '/path/to/logfolder'

#   Initialize Loggefy
logger = Log(title="MyProject", version="1.0", console=True, notify=True)

#   Log various types of messages
logger.info("This is an informative message.", subtitle="Info")
logger.warn("This is a warning message.", subtitle="Warning")
logger.error("This is an error message.", subtitle="Error")
```
---

*Note: To use Loggefy, ensure you have the required dependencies installed, including the `gi.repository` for notifications.*
