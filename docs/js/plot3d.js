const posX = dataset.map(obj => obj.posX)
const posY = dataset.map(obj => obj.posY)
const xAlvo = dataset.map(obj => obj.xAlvo)

plot({
    x: posX,
    y: posY,
    z: xAlvo,
    type: 'scatter3d',
    marker: {
        color: '#0050ef'
    }
})