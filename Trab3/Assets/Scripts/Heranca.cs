using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System.IO;

public class Heranca : MonoBehaviour
{
    public bool txtCriado = false;
    public List<Vector2> listaProjetil = new List<Vector2>();
    public List<Vector2> listaProjetilPontos = new List<Vector2>();

    public void WriteProjectile()
    {
        string path = "Export/projectile.txt";
        StreamWriter writer = new StreamWriter(path, true);
        string x = "x = np.array([";
        string y = "y = np.array([";

        string xPonto = "xPonto = np.array([";
        string yPonto = "yPonto = np.array([";
        foreach (Vector2 i in this.listaProjetil)
        {
            
            x += i.x + ",";
            y += i.y + ",";

        }
        foreach (Vector2 i in this.listaProjetilPontos)
        {

            xPonto += i.x + ",";
            yPonto += i.y + ",";

        }
        x += "])";
        y += "])";
        xPonto += "])";
        yPonto += "])";

        writer.WriteLine(x);
        writer.WriteLine(y);
        writer.WriteLine(xPonto);
        writer.WriteLine(yPonto);
        writer.Close();

    }
}
