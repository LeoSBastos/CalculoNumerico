const xAlvo = dataset.map(obj => obj.xAlvo)
const angulo = dataset.map(obj => obj.angulo)

plot({
    y: xAlvo,
    x: angulo,
    marker: {
        color: '#0050ef'
    }
})
