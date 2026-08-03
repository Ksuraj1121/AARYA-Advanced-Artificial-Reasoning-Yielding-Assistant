import QtQuick

Item {
    width: 260
    height: 260

    // Rotating Ring
    Item {
        id: ringGroup

        anchors.centerIn: parent

        width: 260
        height: 260

        RotationAnimator {
            target: ringGroup
            from: 0
            to: 360
            duration: 6000
            loops: Animation.Infinite
            running: true
        }

        Rectangle {
            anchors.centerIn: parent

            width: 220
            height: 220

            radius: 110

            color: "transparent"

            border.width: 3
            border.color: "#00D9FF"
        }

        // Visible rotating dots
        Repeater {
            model: 4

            Rectangle {
                width: 12
                height: 12

                radius: 6

                color: "#00D9FF"

                x: 124 + Math.cos(index * Math.PI / 2) * 104
                y: 124 + Math.sin(index * Math.PI / 2) * 104
            }
        }
    }

    // AI Core
    Rectangle {
        id: core

        anchors.centerIn: parent

        width: 120
        height: 120

        radius: 60

        color: "#00D9FF"

        SequentialAnimation on scale {
            loops: Animation.Infinite

            NumberAnimation {
                to: 1.08
                duration: 900
            }

            NumberAnimation {
                to: 1.0
                duration: 900
            }
        }

        Text {
            anchors.centerIn: parent

            text: "A"

            color: "black"

            font.pixelSize: 56
            font.bold: true
        }
    }
}