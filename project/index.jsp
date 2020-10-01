<?xml version="1.0" encoding="UTF-8"?>


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
 "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
































<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Stanford Parser</title>
    <style type="text/css">
       div.parserOutput { padding-left: 3em;
                          padding-top: 1em; padding-bottom: 0;
                          margin: 0; }
       div.parserOutputMonospace {
                          padding-top: 1em; padding-bottom: 1em; margin: 0;
                          font-family: monospace; padding-left: 3em; }
       .spacingFree { padding: 0; margin: 0; }
    </style>

    <link href="http://nlp.stanford.edu/nlp.css" rel="stylesheet"
          type="text/css" />

    <script type="text/javascript">
    //<![CDATA[
    

    function showSample() {
      query = document.getElementById("query");
      parserSelect = document.getElementById("parserSelect");
      query.value = document.getElementById("defaultQuery."+
                 parserSelect.selectedIndex).value;
    }

    function handleOnChangeParserSelect() {
      query = document.getElementById("query");
      parserSelect = document.getElementById("parserSelect");
      for (var i = 0; i < 5; i++) {
        defaultQuery = document.getElementById("defaultQuery." + i);
        if (query.value == defaultQuery.value) {
          showSample();
          break;
        }
      }
      parseButton = document.getElementById("parseButton");
      chineseParseButton = document.getElementById("chineseParseButton");
      if (parserSelect.value == "Chinese") {
         parseButton.value = chineseParseButton.value;
      } else {
         parseButton.value = "Parse";
      }
    }
    //]]>
    </script>

    <link rel="icon" type="image/x-icon" href="/parser/favicon.ico" />
    <link rel="shortcut icon" type="image/x-icon"
       href="/parser/favicon.ico" />

  </head>

  <body>
    

    <h1>Stanford Parser</h1>

    <div style="margin-top: 2em;">
    <form action="http://nlp.stanford.edu:8080/parser/index.jsp" method="post">
    <div style="width: 410px;">
    
       <input type="hidden" name="defaultQuery.0"
              id="defaultQuery.0"
              value="هذا الرجل هو سعيد." />
    
       <input type="hidden" name="defaultQuery.1"
              id="defaultQuery.1"
              value="猴子喜欢吃香蕉。" />
    
       <input type="hidden" name="defaultQuery.2"
              id="defaultQuery.2"
              value="paper on information retrieval and data mining" />
    
       <input type="hidden" name="defaultQuery.3"
              id="defaultQuery.3"
              value="Au fond, les choses sont assez simples." />
    
       <input type="hidden" name="defaultQuery.4"
              id="defaultQuery.4"
              value="El reino canta muy bien." />
    
        <input type="hidden" name="chineseParseButton"  id="chineseParseButton"
               value = "&#21078;&#26512; (Parse)" />
        <div>
        Please enter a sentence to be parsed: <br/>
        <textarea name="query" id="query"
         style="width: 400px; height: 8em"
         rows="31" cols="7">paper on information retrieval and data mining</textarea>
        </div>
        <div style="float: left">
        Language:
        <select name="parserSelect" id="parserSelect"
         onchange="handleOnChangeParserSelect();" >
        
           <option value="Arabic" >Arabic</option>
        
           <option value="Chinese" >Chinese</option>
        
           <option value="English" selected="selected">English</option>
        
           <option value="French" >French</option>
        
           <option value="Spanish" >Spanish</option>
        
        </select>
        </div>

        <div style="float: left; padding-left: 2em;">
        <a href="#sample" onclick="showSample();">Sample Sentence</a>
        </div>

        <div style="float: right">
        
           <input type="submit" value="Parse" name="parse" id="parseButton"/>
        
        </div>
      </div>
    </form>
    </div>

    <div style="clear: left; margin-top: 3em">
    

      <h3>Your query</h3>
      <div class="parserOutput"><em>paper on information retrieval and data mining</em></div>

      
          <h3>Tagging</h3>
          <div class="parserOutputMonospace">
          
                 <div style="padding-right: 1em; float: left; white-space: nowrap;">
                 My/PRP$</div>
          
                 <div style="padding-right: 1em; float: left; white-space: nowrap;">
                 dog/NN</div>
          
                 <div style="padding-right: 1em; float: left; white-space: nowrap;">
                 also/RB</div>
          
                 <div style="padding-right: 1em; float: left; white-space: nowrap;">
                 likes/VBZ</div>
          
                 <div style="padding-right: 1em; float: left; white-space: nowrap;">
                 eating/VBG</div>
          
                 <div style="padding-right: 1em; float: left; white-space: nowrap;">
                 sausage/NN</div>
          
                 <div style="padding-right: 1em; float: left; white-space: nowrap;">
                 ./.</div>
          
          </div>

          <div style="clear: left"> </div>
          <h3>Parse</h3>
          <div class="parserOutput">
          <pre id="parse" class="spacingFree">(ROOT
  (S
    (NP (PRP$ My) (NN dog))
    (ADVP (RB also))
    (VP (VBZ likes)
      (S
        (VP (VBG eating)
          (NP (NN sausage)))))
    (. .)))</pre>
          </div>

          

          <h3>Universal dependencies</h3>
          <div class="parserOutput">
          <pre class="spacingFree">nmod:poss(dog-2, My-1)
nsubj(likes-4, dog-2)
advmod(likes-4, also-3)
root(ROOT-0, likes-4)
xcomp(likes-4, eating-5)
dobj(eating-5, sausage-6)</pre>
          </div>

          <h3>Universal dependencies, enhanced</h3>
          <div class="parserOutput">
          <pre class="spacingFree">nmod:poss(dog-2, My-1)
nsubj(likes-4, dog-2)
advmod(likes-4, also-3)
root(ROOT-0, likes-4)
xcomp(likes-4, eating-5)
dobj(eating-5, sausage-6)</pre>
          </div>
          

          <h3>Statistics</h3>

          <br />Tokens: 7 <br /> Time: 0.021 s <br />
          Parser: englishPCFG.ser.gz <br />

        
  </div>

  

  <p>
    <em><a href="http://nlp.stanford.edu/software/lex-parser.shtml">Back to parser home</a></em>
    <br/>
    <em>Last updated 2016-09-12</em>
  </p>

  <p style="text-align: right">
    <a href="http://validator.w3.org/check?uri=referer"><img
        style="border: 0"
        src="http://www.w3.org/Icons/valid-xhtml10"
        alt="Valid XHTML 1.0 Strict" height="31" width="88" /></a>
  </p>
  </body>

	<script>
		document.getElementById("parseButton").click();
	</script>

</html>











