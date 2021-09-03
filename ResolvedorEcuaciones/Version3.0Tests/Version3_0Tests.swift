//
//  Version3_0Tests.swift
//  Version3.0Tests
//
//  Created by user194091 on 9/1/21.
//


    
import XCTest
@testable import Version3_0

class EqSolverTests: XCTestCase{

    let Version3_0 = Solver()
        
        func test1() throws {
            // Given
            let a = 2.0
            let b = 6.0
            let c = 9.0
            
            // When
            let resultado = Version3_0.quadraticSolver(a: a, b: b, c: c)
            
            // Then
            let expectedValue: String = "Raiz 1 = 0.0i Raiz 2 = -3.0i"
            
            XCTAssertEqual(resultado, expectedValue)
        }
    
        func test2() throws {
            // Given
            let a = 4.0
            let b = 2.0
            let c = 2.0
            
            // When
            let resultado = Version3_0.quadraticSolver(a: a, b: b, c: c)
            
            // Then
            let expectedValue: String = "Raiz 1 = 0.411i Raiz 2 = -0.911i"
            
            XCTAssertEqual(resultado, expectedValue)
        }
}
