//
//  ViewController.swift
//  Version3.0
//
//  Created by user194091 on 9/1/21.
//

import UIKit

class ViewController: UIViewController {	

    let solvedor = Solver()
    
    @IBOutlet weak var a: UITextField!
    
    @IBOutlet weak var b: UITextField!
    
    @IBOutlet weak var c: UITextField!
    
    @IBOutlet weak var resolver: UIButton!

    @IBOutlet weak var resultado: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        self.view.endEditing(true)
    }
    
    
    @IBAction func resolver(_ sender: Any) {
        
            view.endEditing(true)
            let A = strtod(a.text,nil)
            let B = strtod(b.text,nil)
            let C = strtod(c.text,nil)
        let result = solvedor.quadraticSolver(a: A, b: B, c: C)
            resultado.text = result
    }
}


    
