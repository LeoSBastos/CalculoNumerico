using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveTarget : Heranca {

    public GameObject target;
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
        if (Input.GetKeyDown(KeyCode.Space)) {
            target.transform.position = new Vector3(Random.Range(-7, 8), target.transform.position.y, target.transform.position.z);
            base.txtCriado = false;
        }
	}
}
