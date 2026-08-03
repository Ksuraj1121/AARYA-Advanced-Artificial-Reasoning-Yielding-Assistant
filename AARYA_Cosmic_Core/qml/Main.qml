import QtQuick
import QtQuick.Window
import "components"

Window {
    visible: true
    width: 1600
    height: 900
    title: "AARYA Cosmic Core"

    color: "#05070A"

    Rectangle {
        anchors.fill: parent
        color: "#05070A"

        AICore {
            anchors.centerIn: parent
        }
    }
}