# Assuming you are using a webview library like PyQt or Tkinter's webview
# Example using CSS to hide the scrollbar

def hide_scrollbar(webview):
    css = """
    <style>
        ::-webkit-scrollbar {
            display: none;
        }
        body {
          -ms-overflow-style: none;  /* IE and Edge */
          scrollbar-width: none;  /* Firefox */
        }
    </style>
    """
    webview.run_javascript(f"var styleTag = document.createElement('style'); styleTag.innerHTML = '{css}'; document.head.appendChild(styleTag);")

# Call this function after the webview is loaded
# hide_scrollbar(your_webview_instance)
