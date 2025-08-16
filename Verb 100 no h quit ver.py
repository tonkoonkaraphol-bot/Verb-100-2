import streamlit as st

# Your verb dictionary remains the same. It is the data for our app.
verb_dictionary = {
    "be": ["was, were", "been"],
    "bear": ["bore", "born"],
    "beat": ["beat", "beaten"],
    "become": ["became", "become"],
    "beget": ["begot", "begotten"],
    "begin": ["began", "begun"],
    "bend": ["bent", "bent"],
    "beseech": ["besought", "besought"],
    "beset": ["beset", "beset"],
    "bet": ["bet", "bet"],
    "bite": ["bit", "bitten"],
    "break": ["broke", "broken"],
    "bring": ["brought", "brought"],
    "browbeat": ["browbeat", "browbeaten"],
    "build": ["built", "built"],
    "buy": ["bought", "bought"],
    "catch": ["caught", "caught"],
    "choose": ["chose", "chosen"],
    "come": ["came", "come"],
    "cut": ["cut", "cut"],
    "do": ["did", "done"],
    "draw": ["drew", "drawn"],
    "drink": ["drank", "drunk"],
    "drive": ["drove", "driven"],
    "eat": ["ate", "eaten"],
    "fall": ["fell", "fallen"],
    "feed": ["fed", "fed"],
    "feel": ["felt", "felt"],
    "find": ["found", "found"],
    "fly": ["flew", "flown"],
    "fight": ["fought", "fought"],
    "forget": ["forgot", "forgotten"],
    "forgive": ["forgave", "forgiven"],
    "get": ["got", "gotten"],
    "give": ["gave", "given"],
    "go": ["went", "gone"],
    "grow": ["grew", "grown"],
    "have": ["had", "had"],
    "hear": ["heard", "heard"],
    "hit": ["hit", "hit"],
    "hold": ["held", "held"],
    "hurt": ["hurt", "hurt"],
    "keep": ["kept", "kept"],
    "know": ["knew", "known"],
    "learn": ["learnt", "learnt"],
    "leave": ["left", "left"],
    "lose": ["lost", "lost"],
    "make": ["made", "made"],
    "meet": ["met", "met"],
    "mistake": ["mistook", "mistaken"],
    "overcome": ["overcame", "overcome"],
    "overdo": ["overdid", "overdone"],
    "oversee": ["oversaw", "overseen"],
    "overtake": ["overtook", "overtaken"],
    "pay": ["paid", "paid"],
    "put": ["put", "put"],
    "read": ["read", "read"],
    "redo": ["redid", "redone"],
    "remake": ["remade", "remade"],
    "retake": ["retook", "retaken"],
    "ride": ["rode", "ridden"],
    "ring": ["rang", "rung"],
    "rise": ["rose", "risen"],
    "run": ["ran", "run"],
    "say": ["said", "said"],
    "see": ["saw", "seen"],
    "seek": ["sought", "sought"],
    "sell": ["sold", "sold"],
    "send": ["sent", "sent"],
    "shave": ["shaved", "shaven"],
    "show": ["showed", "shown"],
    "sing": ["sang", "sung"],
    "sit": ["sat", "sat"],
    "sleep": ["slept", "slept"],
    "speak": ["spoke", "spoken"],
    "spend": ["spent", "spent"],
    "spread": ["spread", "spread"],
    "spring": ["sprang", "sprung"],
    "stand": ["stood", "stood"],
    "steal": ["stole", "stolen"],
    "string": ["strung", "strung"],
    "swear": ["swore", "sworn"],
    "sweat": ["sweat", "sweat"],
    "swim": ["swam", "swum"],
    "take": ["took", "taken"],
    "teach": ["taught", "taught"],
    "tell": ["told", "told"],
    "think": ["thought", "thought"],
    "throw": ["threw", "thrown"],
    "tread": ["trod", "trodden"],
    "undergo": ["underwent", "undergone"],
    "understand": ["understood", "understood"],
    "undertake": ["undertook", "undertaken"],
    "underwrite": ["underwrote", "underwritten"],
}


# --- START of Streamlit UI Code ---

# Add a title to the page using st.title
st.title("Irregular Verb Dictionary")
# Add an introductory message using st.write
st.write("Type an irregular verb to see its other forms. The results will appear as you type.")

# Use st.text_input to get user input from the web interface
user_input = st.text_input("Enter a verb: ").strip().lower()

# The rest of the logic is similar, but we'll use st.write to display the results.
if user_input:  # Check if the user has entered anything
    if user_input in verb_dictionary:
        verb_forms = verb_dictionary[user_input]
        verb2 = verb_forms[0]
        verb3 = verb_forms[1]
        
        # Use st.write or st.markdown to display the output
        st.write(f"**Verb 1:** {user_input}")
        st.write(f"**Verb 2:** {verb2}")
        st.write(f"**Verb 3:** {verb3}")
    else:
        st.write(f"Sorry, I couldn't find '{user_input}' in the dictionary.")
        st.write("Please try a different word.")
