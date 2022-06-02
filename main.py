from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent

from cases import *


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, _):
        items = []
        query = event.get_query() or ''
        query = query.replace(event.get_keyword() + ' ', '', 1)

        if query:
            for case, convert in cases.items():
                converted_query = convert(query)
                copyToClipboardAction = CopyToClipboardAction(converted_query)
                items.append(ExtensionResultItem(
                    icon="images/empty.svg",
                    name=converted_query,
                    description=case,
                    on_enter=copyToClipboardAction,
                    on_alt_enter=copyToClipboardAction,
                    highlightable=False,
                ))

        return RenderResultListAction(items)


class CaseConverterExtension(Extension):
    def __init__(self):
        super(CaseConverterExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


if __name__ == '__main__':
    CaseConverterExtension().run()
