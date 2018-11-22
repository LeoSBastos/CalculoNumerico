const posX = dataset.map(obj => obj.posX)
const posY = dataset.map(obj => obj.posY)
const xAlvo = dataset.map(obj => obj.xAlvo)
const angulo = dataset.map(obj => obj.angulo)

 plot({
 	x: posX,
 	y: posY,
 	z: xAlvo,
 	type: 'scatter3d'
 })

//plot({
//	y: xAlvo,
//	x: angulo
//})