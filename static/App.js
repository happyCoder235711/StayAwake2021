    // month = "Feb"
    // day =  "16"
    // dateVar = month + "/" + day
    console.log("logpog");
    var db = firebase.firestore();

    function addData(x) {
        db.collection("dataA").add({
            title: document.getElementById("titleID").value,
            data: x,
            created: firebase.firestore.FieldValue.serverTimestamp()
        })
        .then((docRef) => {
            console.log("Document written with ID: ", docRef.id);
        })
        .catch((error) => {
            console.error("Error adding document: ", error);
        });
    }
  
    tickerWow = 1
    // create element & render cafe
    function populateListA(doc){
        let name = doc.data().title;
        let date = doc.data().created.toDate().toString();
        let data = doc.data().data.toString();
        tickerWowString = tickerWow.toString();
        document.getElementById(tickerWowString + "Link").setAttribute("href","/graph/"+data)
        console.log("LOGGERSPOGGERS")
        console.log(document.getElementById(tickerWowString + "Link").href)
        document.getElementById(tickerWowString).textContent=(name+", "+date);
        tickerWow = tickerWow + 1;
        console.log("BEEEP BOOP BEEP")


        //document.getElementById(tickerWowString + "Link").title = data;
    }
    
    function onloadThing(){
        db.collection('dataA').orderBy("created", "desc").limit(5).get().then(snapshot => {
            snapshot.docs.forEach(doc => {
                populateListA(doc);
            });
        });
    }
