import logging
import string
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction

logger = logging.getLogger(__name__)


class WordCounterExtension(Extension):

    def __init__(self):
        logger.info('init Word counter extension')
        super(WordCounterExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        rawstr = event.get_argument()
        if rawstr is None:
            rawstr = ""

        total_chars = str(len(rawstr))
        total_words = str(sum(word.strip() for word in rawstr.split()))
        total_words_without_punctuation = str(sum(word.strip(string.punctuation).isalnum() for word in rawstr.split()))
        total_words_without_numeric = str(sum(word.strip(string.punctuation).isalpha() for word in rawstr.split()))
        total_sentences = str(sum(word.strip() for word in rawstr.split(".")))

        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name=total_chars,
                                         description='Chars',
                                         highlightable=False,
                                         on_enter=CopyToClipboardAction(total_chars)
                                         ))

        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name=total_words,
                                         description='Words',
                                         highlightable=False,
                                         on_enter=CopyToClipboardAction(total_words)
                                         ))

        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name=total_words_without_punctuation,
                                         description='Words (without punctuation)',
                                         highlightable=False,
                                         on_enter=CopyToClipboardAction(total_words_without_punctuation)
                                         ))

        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name=total_words_without_numeric,
                                         description='Words (alpha only)',
                                         highlightable=False,
                                         on_enter=CopyToClipboardAction(total_words_without_numeric)
                                         ))

        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name=total_sentences,
                                         description='Sentences',
                                         highlightable=False,
                                         on_enter=CopyToClipboardAction(total_sentences)
                                         ))

        return RenderResultListAction(items)


if __name__ == '__main__':
    WordCounterExtension().run()
