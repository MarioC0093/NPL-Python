def get_ner_in_context(keyword, document, desired_ner_labels= False):
    
    if desired_ner_labels != False:
        desired_ner_labels = desired_ner_labels
    else:
         # all possible labels
        desired_ner_labels = list(nlp.get_pipe('ner').labels)
        
    i=0
        
    #Iterate through all the sentences in the document and pull out the text of each sentence
    for sentence in document.sents:
        #process each sentence
        sentence_doc = nlp(sentence.text)
        for named_entity in sentence_doc.ents:
            #Check to see if the keyword is in the sentence (and ignore capitalization by making both lowercase)
            if keyword.lower() in named_entity.text.lower()  and named_entity.label_ in desired_ner_labels:
                i=i+1
                #Use the regex library to replace linebreaks and to make the keyword bolded, again ignoring capitalization
            
                sentence_text = re.sub('\n', ' ', sentence.text)
                sentence_text = re.sub(f"{named_entity.text}", f"**{named_entity.text}**", sentence_text, flags=re.IGNORECASE)

                display(Markdown(f'**Resultado {i}.**')) # Si pones --- te sale una línea de izq a drcha
                display(Markdown(f"Tipo de entidad: **{named_entity.label_}**"))
                display(Markdown('Contexto:'))
                display(Markdown(sentence_text))