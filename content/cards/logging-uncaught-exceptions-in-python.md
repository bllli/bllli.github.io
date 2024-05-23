---
title: python  Logging uncaught exceptions in Python
date created: 2023-12-29 23:10
date modified: 2024-05-23 21:12
slug: logging-uncaught-exceptions-in-python
---

#Area/RD/backend/python

https://stackoverflow.com/questions/6234405/logging-uncaught-exceptions-in-python/16993115#16993115



```python
    def handle_exception(exc_type, exc_value, exc_traceback):
        """
        Log any uncaught exception instead of letting it be printed by Python
        (but leave KeyboardInterrupt untouched to allow users to Ctrl+C to stop)
        See https://stackoverflow.com/a/16993115/3641865
        """
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return

        root_logger.error(
            "Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback)
        )

    sys.excepthook = handle_exception


```