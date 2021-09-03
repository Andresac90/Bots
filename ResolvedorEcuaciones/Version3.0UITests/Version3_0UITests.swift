//
//  Version3_0UITests.swift
//  Version3.0UITests
//
//  Created by user194091 on 9/1/21.
//

import XCTest

class Version3_0UITests: XCTestCase {

    override func setUpWithError() throws {
        // Put setup code here. This method is called before the invocation of each test method in the class.

        // In UI tests it is usually best to stop immediately when a failure occurs.
        continueAfterFailure = false

        // In UI tests it’s important to set the initial state - such as interface orientation - required for your tests before they run. The setUp method is a good place to do this.
    }

    override func tearDownWithError() throws {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
    }

    func testExample() throws {
        // UI tests must launch the application that they test.
        let app = XCUIApplication()
        app.launch()

        // Use recording to get started writing UI tests.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
    }

    func testLaunchPerformance() throws {
        if #available(macOS 10.15, iOS 13.0, tvOS 13.0, *) {
            // This measures how long it takes to launch your application.
            measure(metrics: [XCTApplicationLaunchMetric()]) {
                XCUIApplication().launch()
            }
        }
    }
    func testEquationSolverThreeCoeffs() throws {
          let app = XCUIApplication()
          app.launch()
          
          let aTextField = app.textFields["A"]
          let bTextField = app.textFields["B"]
          let cTextField = app.textFields["C"]
          let raiz1TextField = app.textFields["Resultado"]
        
          aTextField.tap()
          aTextField.typeText("6.0")
          bTextField.tap()
          bTextField.typeText("-3.0")
          cTextField.tap()
          cTextField.typeText("3.0")
          app.staticTexts["Resolver"].tap()

          print("Raiz1 " + (raiz1TextField.value as! String))

        XCTAssertEqual(raiz1TextField.value as! String, "Raiz 1 = 0.911i Raiz 2 = -0.411i")
          
      }
    
    func testEquationSolverThreeCoeffs2() throws {
          let app = XCUIApplication()
          app.launch()
          
          let aTextField = app.textFields["A"]
          let bTextField = app.textFields["B"]
          let cTextField = app.textFields["C"]
          let raiz1TextField = app.textFields["Resultado"]
        
          aTextField.tap()
          aTextField.typeText("8.0")
          bTextField.tap()
          bTextField.typeText("10.0")
          cTextField.tap()
          cTextField.typeText("20.0")
          app.staticTexts["Resolver"].tap()

          print("Raiz1 " + (raiz1TextField.value as! String))

        XCTAssertEqual(raiz1TextField.value as! String, "Raiz 1 = 0.827i Raiz 2 = -2.077i")
          
      }
}
