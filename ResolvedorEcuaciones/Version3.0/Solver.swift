//
//  Solver.swift
//  Version3.0
//
//  Created by user194091 on 9/2/21.
//

import Foundation

public class Solver {
    public func quadraticSolver(a: Double, b: Double, c: Double) -> String {
        if abs(a) < 0.00001 {
            let result = 0
            return "\(result)"
        }
        let b2_4ac = b*b - (4*a*c)
        if b2_4ac == 0 {
            let result = -b/(2*a)
            return "Solo existe un resultado: \(result)"
        }
        if b2_4ac < 0 {
            let b2_4ac = b2_4ac * (-1)
            let sq = sqrt(b2_4ac)
            let root1 = (-b + sq) / (2 * a)
            let root2 = (-b - sq) / (2 * a)
            return "Raiz 1 = \(round(1000 * root1)/1000)i \n Raiz 2 = \(round(1000 * root2)/1000)i"
        }
        let sq = sqrt(b2_4ac)
        let root1 = (-b + sq) / (2 * a)
        let root2 = (-b - sq) / (2 * a)
        return "Raiz 1 = \(root1) Raiz 2 = \(root2)"
    }
}

