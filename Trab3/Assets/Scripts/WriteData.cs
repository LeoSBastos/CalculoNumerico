using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using UnityEditor;



public class WriteData {
    int i = 0;
    public struct Dados
    {
        public float angulo;
        public float x;
        public float y;
        public float xAlvo;
    }
    public Dados d;
    public List<Dados> listaDados = new List<Dados>();
    public void PopulaLista()
    {
        this.listaDados.Add(this.d);
    }

    public void CriaTxt() {
        string path = "Export/dataset.js";
        StreamWriter writer = new StreamWriter(path, true);
        int j = 0;

        writer.WriteLine("const dataset = [");
        foreach (Dados d in this.listaDados)
        {
            writer.WriteLine("{");
            writer.WriteLine("\"angulo\": " + d.angulo+ ",");
            writer.WriteLine("\"posX\": " + d.x + ",");
            writer.WriteLine("\"posY\": " + d.y + ",");
            writer.WriteLine("\"xAlvo\": " + d.xAlvo);
            writer.WriteLine("},");
            j++;
        }
        i++;
        writer.WriteLine("]");
        writer.Close();
        
    }
}
