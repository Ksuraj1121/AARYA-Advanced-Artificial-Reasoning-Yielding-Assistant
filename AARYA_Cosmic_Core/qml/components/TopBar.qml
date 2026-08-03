import QtQuick
import QtQuick.Controls
import "."

Rectangle {
    width: parent.width
    height: 70

    color: "#0A1118"
    border.color: "#00D9FF"
    border.width: 1
    opacity: 0.92

    // Left Logo
    Text {
        anchors.left: parent.left
        anchors.leftMargin: 30
        anchors.verticalCenter: parent.verticalCenter

        text: "A A R Y A"
        color: "#00D9FF"
        font.pixelSize: 30
        font.bold: true
    }

    // Center Live Clock
    Clock {
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
    }

    // Right Icons
    Row {
        anchors.right: parent.right
        anchors.rightMargin: 30
        anchors.verticalCenter: parent.verticalCenter

        spacing: 15

        Rectangle {
            width: 40
            height: 40
            radius: 20

            color: "#111F2C"
            border.color: "#00D9FF"

            Text {
                anchors.centerIn: parent
                text: "⚙"
                color: "white"
                font.pixelSize: 18
            }

            MouseArea {
                anchors.fill: parent
                hoverEnabled: true

                onEntered: parent.color = "#16354F"
                onExited: parent.color = "#111F2C"
            }
        }

        Rectangle {
            width: 40
            height: 40
            radius: 20

            color: "#111F2C"
            border.color: "#00D9FF"

            Text {
                anchors.centerIn: parent
                text: "👤"
                color: "white"
                font.pixelSize: 18
            }

            MouseArea {
                anchors.fill: parent
                hoverEnabled: true

                onEntered: parent.color = "#16354F"
                onExited: parent.color = "#111F2C"
            }
        }
    }
}