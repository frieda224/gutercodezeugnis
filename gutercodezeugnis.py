<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<title>Zeugnisrechner</title>
<style>
    body {
        font-family: Arial, sans-serif;
        background: #f4f4f4;
        padding: 20px;
    }

    h1 {
        text-align: center;
    }

    .fach {
        display: flex;
        gap: 10px;
        margin-bottom: 10px;
    }

    input, select, button {
        padding: 6px;
        font-size: 14px;
    }

    .note {
        width: 80px;
        text-align: center;
        font-weight: bold;
    }

    .gut { background-color: #b6f2b6; }
    .mittel { background-color: #ffd699; }
    .schlecht { background-color: #f2b6b6; }

    #durchschnitt {
        margin-top: 20px;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
    }
</style>
</head>
<body>

<h1>Zeugnisdurchschnitt berechnen</h1>

<label>Notensystem:</label>
<select id="system">
    <option value="noten">Noten (1–6)</option>
    <option value="punkte">Notenpunkte (0–15)</option>
</select>

<div id="faecher"></div>

<button onclick="fachHinzufuegen()">Fach hinzufügen</button>
<button onclick="berechnen()">Durchschnitt berechnen</button>

<div id="durchschnitt"></div>

<script>
function fachHinzufuegen() {
    const div = document.createElement("div");
    div.className = "fach";

    div.innerHTML = `
        <input type="text" placeholder="Fach">
        <input type="number" class="note">
    `;

    document.getElementById("faecher").appendChild(div);
}

function berechnen() {
    const system = document.getElementById("system").value;
    const notenFelder = document.querySelectorAll(".note");

    let summe = 0;
    let anzahl = 0;

    notenFelder.forEach(feld => {
        const wert = Number(feld.value);
        if (!isNaN(wert)) {
            summe += wert;
            anzahl++;

            feld.classList.remove("gut", "mittel", "schlecht");

            if (system === "noten") {
                if (wert <= 2) feld.classList.add("gut");
                else if (wert <= 4) feld.classList.add("mittel");
                else feld.classList.add("schlecht");
            } else {
                if (wert >= 10) feld.classList.add("gut");
                else if (wert >= 5) feld.classList.add("mittel");
                else feld.classList.add("schlecht");
            }
        }
    });

    if (anzahl === 0) {
        document.getElementById("durchschnitt").innerText =
            "Bitte Noten eingeben.";
        return;
    }

    const durchschnitt = (summe / anzahl).toFixed(2);
    document.getElementById("durchschnitt").innerText =
        "Durchschnitt: " + durchschnitt;
}
</script>

</body>
</html>
