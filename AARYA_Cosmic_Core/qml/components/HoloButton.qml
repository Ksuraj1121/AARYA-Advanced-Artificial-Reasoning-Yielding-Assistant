import QtQuick

Rectangle {

    id: root

    width: 180
    height: 48
    radius: 8

    property alias text: buttonText.text

    color: "#111F2C"
    border.color: "#00D9FF"
    border.width: 1

    Behavior on color {
        ColorAnimation { duration: 180 }
    }

    Behavior on scale {
        NumberAnimation { duration: 120 }
    }

    Text {
        id: buttonText
        anchors.centerIn: parent
        color: "white"
        font.pixelSize: 16
        font.bold: true
    }

    MouseArea {
        anchors.fill: parent
        hoverEnabled: true

        onEntered: {
            root.color = "#1A4C73"
            root.scale = 1.05
        }

        onExited: {
            root.color = "#111F2C"
            root.scale = 1.0
        }

        onPressed: root.scale = 0.96
        onReleased: root.scale = 1.05
    }
}