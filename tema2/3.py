def numara_ocurrente(subsir, sir_principal):
    return sir_principal.count(subsir)

primul_sir = input("Introdu primul șir (subsir): ")
al_doilea_sir = input("Introdu al doilea șir (șir principal): ")
ocurrente = numara_ocurrente(primul_sir, al_doilea_sir)
print(f"Subșirul '{primul_sir}' apare de {ocurrente} ori în șirul principal.")
