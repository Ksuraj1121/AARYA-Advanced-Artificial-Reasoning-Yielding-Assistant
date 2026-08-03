import QtQuick
import "components"

Item {

    anchors.fill: parent

    // Star Background
    StarField {
        anchors.fill: parent
    }

    // Top Bar
    TopBar {
        anchors.top: parent.top
        width: parent.width
    }

    // Left Menu
    SideMenu {
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.topMargin: 80
        anchors.bottom: parent.bottom
    }

    // Right Status Panel
    StatusPanel {
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.topMargin: 80
        anchors.bottom: parent.bottom
    }

    // Welcome Text
    WelcomeText {
        anchors.horizontalCenter: parent.horizontalCenter
        y: 90
    }

    // Center AI Core with Glow
    Item {
        anchors.centerIn: parent
        width: 320
        height: 320

        Glow {
            anchors.centerIn: parent
        }

        AICore {
            anchors.centerIn: parent
        }
    }
}