# AWS_Data


   <!-- http://www.owl-ontologies.com/Ontology1263829566.owl#Binod -->

    <owl:NamedIndividual rdf:about="http://www.owl-ontologies.com/Ontology1263829566.owl#Binod">
        <rdf:type rdf:resource="http://www.owl-ontologies.com/Ontology1263829566.owl#NonEUCountry"/>
        <rdf:type rdf:resource="http://www.owl-ontologies.com/Ontology1263829566.owl#NorthAmericanCountry"/>
        <rdf:type rdf:resource="http://www.owl-ontologies.com/Ontology1263829566.owl#NorthAmericanStudent"/>
        <rdf:type rdf:resource="http://www.owl-ontologies.com/Ontology1263829566.owl#Person"/>
        <studies rdf:resource="http://www.owl-ontologies.com/Ontology1263829566.owl#AI"/>
        <studies rdf:resource="http://www.owl-ontologies.com/Ontology1263829566.owl#Automation"/>
        <studies rdf:resource="http://www.owl-ontologies.com/Ontology1263829566.owl#CyberSecurity"/>
        <studies rdf:resource="http://www.owl-ontologies.com/Ontology1263829566.owl#Networking"/>
    </owl:NamedIndividual>



    <!-- http://www.owl-ontologies.com/Ontology1263829566.owl#Mia -->

    <owl:NamedIndividual rdf:about="http://www.owl-ontologies.com/Ontology1263829566.owl#Mia">
        <rdf:type rdf:resource="http://www.owl-ontologies.com/Ontology1263829566.owl#Person"/>
        <rdf:type>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.owl-ontologies.com/Ontology1263829566.owl#studies"/>
                <owl:allValuesFrom>
                    <owl:Class>
                        <owl:oneOf rdf:parseType="Collection">
                            <rdf:Description rdf:about="http://www.owl-ontologies.com/Ontology1263829566.owl#AI"/>
                            <rdf:Description rdf:about="http://www.owl-ontologies.com/Ontology1263829566.owl#EnglishLiterature"/>
                            <rdf:Description rdf:about="http://www.owl-ontologies.com/Ontology1263829566.owl#Programming"/>
                        </owl:oneOf>
                    </owl:Class>
                </owl:allValuesFrom>
            </owl:Restriction>
        </rdf:type>
        <residentOf rdf:resource="http://www.owl-ontologies.com/Ontology1263829566.owl#Japan"/>
        <studies rdf:resource="http://www.owl-ontologies.com/Ontology1263829566.owl#AI"/>
        <studies rdf:resource="http://www.owl-ontologies.com/Ontology1263829566.owl#EnglishLiterature"/>
        <studies rdf:resource="http://www.owl-ontologies.com/Ontology1263829566.owl#Programming"/>
    </owl:NamedIndividual>
