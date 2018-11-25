using UnityEngine;
using System.Collections;
using UnityEngine.UI;
using System.Collections.Generic;



// Classe para controle do projetil (bala de canhao)
// A fisica do projetil fica a cargo da Unity, pelo uso
// do componente Rigidbody 2D.
public class BulletControl : Heranca
{
    // Transform com o limite vertical para os projeteis
    // (obtained by its name)
    private Transform m_verticalLimit;
    private Collider2D coll;
    private Collision2D coli;
    private Rigidbody2D rb;

    void Start()
    {
        listaProjetil.Add(transform.position);
        GameObject obj = GameObject.Find("limit");
        if (!obj)
            throw new UnityException("A instancia do objeto empty chamado 'limit' nao foi encontrada!");
        m_verticalLimit = obj.transform;
        rb = GetComponent<Rigidbody2D>();
        listaProjetilPontos.Add(transform.position);
    }

    // Atualizaçao quadro-a-quadro
    void FixedUpdate()
    {
        // Checa se o projetil atingiu o "chao" (dado pelo posiçao vertical do
        // objeto vazio chamado 'limit'). Se atingiu, destroi o projetil.
        if (transform.position.y <= m_verticalLimit.position.y)
        {
            explode();
        }

        listaProjetil.Add(transform.position);

        if (FastApproximately(rb.velocity.y, float.Parse(0.0.ToString()) , float.Parse(0.1.ToString())))
        {
            listaProjetil.Add(transform.position);
            listaProjetilPontos.Add(transform.position);
        }

    }

    // Captura a colisao com outra bala (via um collider)
    void OnTriggerEnter2D(Collider2D other)
    {
        coll = other;
        explode();
    }

    // Captura a colisao com o alvo (via um trigger)
    void OnCollisionEnter2D(Collision2D other)
    {
        coli = other;
        explode();
        other.transform.position = new Vector3(Random.Range(-7, 8), other.transform.position.y, other.transform.position.z);
        listaProjetil.Add(transform.position);
        listaProjetilPontos.Add(transform.position);
        //this.WriteProjectile();
        base.txtCriado = false;
    }

    // Anima a explosao
    void explode()
    {
        // Toca a animaçao da exploçao (particulas de fogo)
        ParticleSystem explosion = GetComponent<ParticleSystem>();

        if (coli != null)
        {
            explosion.transform.position = coli.transform.position;
        }
        if (coll != null)
        {
            explosion.transform.position = coll.transform.position;
        }

        explosion.Play();


        //Toca o som da explosao
        AudioSource sound = GetComponent<AudioSource>();
        sound.Play();

        // Esconde a bala
        GetComponent<Renderer>().enabled = false;

        // Destroy o objeto apos o fim da animaçao
        Destroy(gameObject, explosion.duration);

        // Destroy (e para) esse script imediatamente
        // (para que o som e as particulas nao encavalem)
        Destroy(this);
    }

    public static bool FastApproximately(float a, float b, float threshold)
    {
        return ((a - b) < 0 ? ((a - b) * -1) : (a - b)) <= threshold;
    }
}
