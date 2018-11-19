using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using UnityEngine.EventSystems;
using UnityEngine.UI;

// Classe para controle do canhao
public class CannonControl : MonoBehaviour
{
	// Prefab do ponto de trajetoria (a ser definido via editor)
	[SerializeField]
	private GameObject m_dotPrefab;

	// Prefab do projetil (a ser definido via editor)
	[SerializeField]
	private GameObject m_bulletPrefab;

	// Objeto do alvo (a ser definido via editor)
    [SerializeField]
    private GameObject m_targetObject;

    //Armazena dx
    float dx;
    //Armazena dy
    float dy;
    //Armazena velocidade
    float speed = 200f;
    

	// Indicativo se a mira deve ser fixada no alvo
	private bool m_fixedInTarget = true;
	
	// Propriedade para permitir alteraçao via checkbox na interface grafica
	public bool fixedInTarget
	{
		get
		{
			return m_fixedInTarget;
		}
		
		set
		{
			m_fixedInTarget = value;
		}
	}

	// Indicaçao de que o mouse esta pressionado
	private bool m_mousePressed = false;

	// Transform com a posiçao da boca do canhao
	private Transform m_cannonMouth;

	// Lista com os pontos de trajetoria utilizados
	private List<GameObject> m_trajectoryPoints;

	// Angulo atual do canhao
	private float m_angle;

	// Transform com o limite vertical para os tracos da trajetoria
	// (obtained by its name)
	private Transform m_verticalLimit;

	// Vetor de força com a qual o tiro sera executado.
	private Vector2 m_force;

	// Inicilizaçao do script
	void Start()
	{
		GameObject obj = GameObject.Find("limit");
		if(!obj)
			throw new UnityException("A instancia do objeto empty chamado 'limit' nao foi encontrada!");
		m_verticalLimit = obj.transform;

		// Procura pelo objeto filho que marca a boca do canhao
		m_cannonMouth = transform.Find("mouth");
		if(!m_cannonMouth)
			throw new UnityException("A instancia do objeto empty chamado 'mouth' nao foi encontrada!");

		// Cria inicialmente 30 pontos de trajetoria (a lista e ajustada dinamicamente
		// conforme a necessidade)
		m_trajectoryPoints = new List<GameObject>();
		for(int i = 0; i < 30; i++)
		{
			GameObject dot = (GameObject) Instantiate(m_dotPrefab);
			dot.GetComponent<Renderer>().enabled = false;
			m_trajectoryPoints.Add(dot);
		}
	}

	// Atualizaçao quadro-a-quadro
	void Update()
	{
        PlayerMoviment();


        // A força de lançamento do projetil e igual ao vetor de distancia do
        // canhao ao ponteiro do mouse.
        Vector3 mousePos = Camera.main.ScreenToWorldPoint(Input.mousePosition);
		Vector2 dirMouse = mousePos - transform.position;
		m_force = dirMouse;

		// Desenha uma linha amarela no scene viewer do editor para indicar
		// visualmente o vetor de força
		Debug.DrawLine(transform.position, mousePos, Color.yellow);

		// Equipara a "altura" do alvo a do canhao
		Vector2 target = m_targetObject.transform.position;
		//target.y = transform.position.y;

		// Calcula os componentes de velocidade x e y
		float mass = m_bulletPrefab.GetComponent<Rigidbody2D>().mass;
		float gravity = Physics.gravity.magnitude;

		float velX = m_force.magnitude / mass;
		float time = (target.x - transform.position.x) / velX;
		float velY = gravity * (time / 2);

		// Calcula o angulo de lançamento
		m_angle = (Mathf.Atan2(velY, velX) * Mathf.Rad2Deg) - 15;

		// Ajusta conforme o angulo em que o tiro "deve" atingir o alvo
		time = (target.x - Mathf.Sin((90 - m_angle) * Mathf.Deg2Rad) - transform.position.x) / velX;
		velY = gravity * (time / 2);

		// Calcula a velocidade e forma finais
		Vector2 velocity = new Vector2(velX, velY);
		m_force = velocity * mass;
		
		// Rotaciona o canhao para o angulo calculado
		transform.rotation = Quaternion.Euler(0f, 0f, m_angle);
        
		showTrajectoryPoints();

		// Captura o pressionamento/liberaçao do botao do mouse
		// (somente se nao estiver sobre o checkbox da UI)
		if(!EventSystem.current.IsPointerOverGameObject())
		{
			if(Input.GetMouseButtonDown(0))
				m_mousePressed = true;
			
			if(Input.GetMouseButtonUp(0))
			{
                m_mousePressed = false;
				shootBullet();
			}
		}
    }

	// Simula o tiro do canhao
	void shootBullet()
	{

		// Cria o projetil e o posiciona na boca do canhao
		GameObject bullet = (GameObject) Instantiate(m_bulletPrefab);
		bullet.transform.position = m_cannonMouth.position;

        // Aplica a força a bala
        Rigidbody2D body = bullet.GetComponent<Rigidbody2D>();
		body.AddForce(m_force, ForceMode2D.Impulse);

		// Toca o som do tiro
		AudioSource sound = GetComponent<AudioSource>();
		sound.Play();
	}

	// Exibe os pontos de trajetoria para a força atual.
	// O angulo do tiro esta embutido no vetor de força.
	void showTrajectoryPoints()
	{
		float mass = m_bulletPrefab.GetComponent<Rigidbody2D>().mass;
		Vector2 velocity = m_force / mass;
		float angle = Mathf.Rad2Deg * (Mathf.Atan2(velocity.y , velocity.x));

		// Esse valor e uma estimativa de quanto de tempo passa a cada "quadro"
		// Na pratica, ele serve pra ajustar a distancia entre os pontos no traçado
		// Quanto mais proximo de zero (so nao pode ser zero mesmo!), mais parecido
		// com uma linha o traçado se torna
		float step = 0.03f;

		float time = 0;
		Vector2 currentPos = m_cannonMouth.position;
		for(int i = 0; i < m_trajectoryPoints.Count; i++)
		{
			GameObject dot = m_trajectoryPoints[i];
			dot.transform.position = currentPos;
			if(currentPos.y >= m_verticalLimit.position.y)
				dot.GetComponent<Renderer>().enabled = true;
			else
				dot.GetComponent<Renderer>().enabled = false;

		    dx = velocity.magnitude * time * Mathf.Cos(angle * Mathf.Deg2Rad);
			dy = velocity.magnitude * time * Mathf.Sin(angle * Mathf.Deg2Rad) - (Physics2D.gravity.magnitude * time * time / 2.0f);

            Text uiDX = GameObject.Find("/Canvas/dx").GetComponent<Text>();
            uiDX.text = dx.ToString();
            Text uiDY = GameObject.Find("/Canvas/dy").GetComponent<Text>();
            uiDY.text = dy.ToString();

            currentPos = new Vector3(m_cannonMouth.position.x + dx , m_cannonMouth.position.y + dy ,2);
			time += step;

            // Ajuste dinamico dos pontos necessarios para traçar a trajetoria.
            // Basicamente: se faltam pontos para alcançar o limite vertical,
            // adiciona mais 10 deles na lista.
            if (i == m_trajectoryPoints.Count - 1 && currentPos.y > m_verticalLimit.position.y)
			{
				for(int j = 0; j < 10; j++)
				{
					dot = (GameObject) Instantiate(m_dotPrefab);
					dot.GetComponent<Renderer>().enabled = true;
					m_trajectoryPoints.Add(dot);
				}
			}
		}
	}


    void PlayerMoviment()
    {
        if (Input.GetKeyDown(KeyCode.D))
        {
            transform.position = new Vector3(transform.position.x + 1, transform.position.y, transform.position.z); 
        }
        if (Input.GetKeyDown(KeyCode.A))
        {
            transform.position = new Vector3(transform.position.x - 1, transform.position.y, transform.position.z);

        }
        


    }
}
