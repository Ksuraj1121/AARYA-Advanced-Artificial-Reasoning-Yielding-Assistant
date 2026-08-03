import QtQuick
import "."

Rectangle {

    width: 220

    color: "#0A1118"
    border.color: "#00D9FF"
    border.width: 1
    radius: 10

    Column {

        anchors.fill: parent
        anchors.margins: 20

        spacing: 15

        HoloButton { text: "🧠 AI Assistant" }
        HoloButton { text: "💾 Memory" }
        HoloButton { text: "📂 Files" }
        HoloButton { text: "🌐 Web" }
        HoloButton { text: "🎤 Voice" }
        HoloButton { text: "👁 Vision" }
        HoloButton { text: "⚙ Settings" }
    }
}