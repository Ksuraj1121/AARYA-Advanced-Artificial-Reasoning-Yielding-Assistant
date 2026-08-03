import QtQuick
import QtQuick.Controls

Rectangle {

    width: 260
    color: "#0A1118"

    border.color: "#00D9FF"
    border.width: 1

    radius: 12
    opacity: 0.95

    Column {

        anchors.fill: parent
        anchors.margins: 20

        spacing: 18

        Text {
            text: "SYSTEM STATUS"

            color: "#00D9FF"
            font.pixelSize: 24
            font.bold: true
        }

        Rectangle {
            width: parent.width
            height: 1
            color: "#1B4C63"
        }

        // CPU

        Text {
            text: "CPU"

            color: "white"
            font.pixelSize: 18
        }

        ProgressBar {
            width: parent.width
            from: 0
            to: 100
            value: backend.cpu
        }

        Text {
            text: backend.cpu.toFixed(1) + " %"

            color: "#00D9FF"
            font.pixelSize: 16
        }

        // RAM

        Text {
            text: "RAM"

            color: "white"
            font.pixelSize: 18
        }

        ProgressBar {
            width: parent.width
            from: 0
            to: 100
            value: backend.ram
        }

        Text {
            text: backend.ram.toFixed(1) + " %"

            color: "#00D9FF"
            font.pixelSize: 16
        }

        // DISK

        Text {
            text: "DISK"

            color: "white"
            font.pixelSize: 18
        }

        ProgressBar {
            width: parent.width
            from: 0
            to: 100
            value: backend.disk
        }

        Text {
            text: backend.disk.toFixed(1) + " %"

            color: "#00D9FF"
            font.pixelSize: 16
        }

        Item {
            width: 1
            height: 20
        }

        Rectangle {
            width: parent.width
            height: 1
            color: "#1B4C63"
        }

        Text {
            text: "AARYA STATUS"

            color: "#00D9FF"
            font.pixelSize: 20
            font.bold: true
        }

        Row {

            spacing: 10

            Rectangle {
                width: 12
                height: 12
                radius: 6

                color: "lime"
            }

            Text {
                text: "ONLINE"

                color: "white"
                font.pixelSize: 16
            }
        }
    }
}