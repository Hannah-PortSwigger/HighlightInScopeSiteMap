from burp import IBurpExtender

class BurpExtender(IBurpExtender):
    def	registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Highlight in-scope Site Map items")

        reqresparr = callbacks.getSiteMap(None)
        for reqresp in reqresparr:
            if callbacks.isInScope(self._helpers.analyzeRequest(reqresp).getUrl()):
                reqresp.setHighlight("green")

        return
