# -*- coding: utf-8 -*-
# Copyright(C)   | Carlos Duarte
# License        | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Source in      | https://github.com/cjdduarte/Disconnected_Review_Log_Cleaner

from aqt import mw
from aqt.qt import QAction
from aqt.utils import showInfo, askUser
from aqt.operations import CollectionOp
from anki.collection import OpChanges
from anki.hooks import addHook
from .translations import tr

def cleanDisconnectedReviewLogs():
    # Count disconnected review log entries
    count = mw.col.db.scalar("SELECT count(*) FROM revlog WHERE cid NOT IN (SELECT id FROM cards)")

    if count == 0:
        showInfo(tr("no_disconnected_found"))
        return

    msg = tr("confirmation_message", count=count)

    if not askUser(msg):
        return

    # Execute mod_schema in main thread BEFORE the async operation
    mw.col.mod_schema(check=True)
    
    # Pre-translate messages to avoid threading issues
    success_msg = tr("success_message", count=count)

    def on_success(result):
        showInfo(success_msg)

    def on_failure(exception):
        showInfo(f"Error: {exception}")

    def operation(col):
        # Only execute the deletion in background thread
        # mod_schema was already called in main thread
        col.db.execute("DELETE FROM revlog WHERE cid NOT IN (SELECT id FROM cards)")
        
        # Return a standard OpChanges object
        return OpChanges()

    # Use CollectionOp instead of manual progress/reset
    CollectionOp(
        parent=mw,
        op=operation,
    ).success(
        on_success
    ).failure(
        on_failure
    ).run_in_background()

def setupMenu():
    """Setup menu after Anki is fully loaded"""
    # Add to Tools menu
    menu_label = tr("menu_label")
    action = QAction(menu_label, mw)
    action.triggered.connect(cleanDisconnectedReviewLogs)
    mw.form.menuTools.addAction(action)

# Hook to setup menu when main window is ready
addHook("profileLoaded", setupMenu)
