//
//  ViewController.swift
//  Good Jobs Nation Test
//
//  Created by Ethan L. Plail on 3/7/17.
//  Copyright © 2017 com.goodjobsnationTesting. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    
    @IBOutlet weak var Webview: UIWebView!
    

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        let aurl = NSURL(string: "https://georgetown.neotalogic.com/a/goodjobnationtesting")
        let request = NSURLRequest(url: aurl as! URL)
        
        Webview.loadRequest(request as URLRequest)
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

