def getConclusion(kp, das, kl, kw, ch, temp):
    result = ""

    if kp == 'tidak padat' and das == 'kecil' and kl == 'landai' and kw == 'rendah' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'landai' and kw == 'rendah' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'landai' and kw == 'rendah' and ch == 'tinggi':
        result = 'banjir'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'landai' and kw == 'sedang' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'landai' and kw == 'sedang' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'landai' and kw == 'sedang' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'landai' and kw == 'tinggi' and ch == 'rendah':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'landai' and kw == 'tinggi' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'landai' and kw == 'tinggi' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'curam' and kw == 'rendah' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'curam' and kw == 'rendah' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'curam' and kw == 'rendah' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'curam' and kw == 'sedang' and ch == 'rendah':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'curam' and kw == 'sedang' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'curam' and kw == 'sedang' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'curam' and kw == 'tinggi' and ch == 'rendah':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'curam' and kw == 'tinggi' and ch == 'sedang':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'curam' and kw == 'tinggi' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'sangat curam' and kw == 'rendah' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'sangat curam' and kw == 'rendah' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'sangat curam' and kw == 'rendah' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'sangat curam' and kw == 'sedang' and ch == 'rendah':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'sangat curam' and kw == 'sedang' and ch == 'sedang':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'sangat curam' and kw == 'sedang' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'sangat curam' and kw == 'tinggi' and ch == 'rendah':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'sangat curam' and kw == 'tinggi' and ch == 'sedang':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'sangat curam' and kw == 'tinggi' and ch == 'tinggi':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'landai' and kw == 'rendah' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'landai' and kw == 'rendah' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'landai' and kw == 'rendah' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'landai' and kw == 'sedang' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'landai' and kw == 'sedang' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'landai' and kw == 'sedang' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'landai' and kw == 'tinggi' and ch == 'rendah':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'landai' and kw == 'tinggi' and ch == 'sedang':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'landai' and kw == 'tinggi' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'curam' and kw == 'rendah' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'curam' and kw == 'rendah' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'curam' and kw == 'rendah' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'curam' and kw == 'sedang' and ch == 'rendah':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'curam' and kw == 'sedang' and ch == 'sedang':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'curam' and kw == 'sedang' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'curam' and kw == 'tinggi' and ch == 'rendah':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'curam' and kw == 'tinggi' and ch == 'sedang':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'curam' and kw == 'tinggi' and ch == 'tinggi':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'sangat curam' and kw == 'rendah' and ch == 'rendah':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'sangat curam' and kw == 'rendah' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'sangat curam' and kw == 'rendah' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'sangat curam' and kw == 'tinggi' and ch == 'rendah':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'sangat curam' and kw == 'tinggi' and ch == 'sedang':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'sedang' and kl == 'sangat curam' and kw == 'tinggi' and ch == 'tinggi':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'landai' and kw == 'rendah' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'landai' and kw == 'rendah' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'landai' and kw == 'rendah' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'landai' and kw == 'sedang' and ch == 'rendah':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'landai' and kw == 'sedang' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'landai' and kw == 'sedang' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'landai' and kw == 'tinggi' and ch == 'rendah':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'landai' and kw == 'tinggi' and ch == 'sedang':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'landai' and kw == 'tinggi' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'curam' and kw == 'rendah' and ch == 'rendah':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'curam' and kw == 'rendah' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'curam' and kw == 'rendah' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'curam' and kw == 'sedang' and ch == 'rendah':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'curam' and kw == 'sedang' and ch == 'sedang':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'curam' and kw == 'sedang' and ch == 'tinggi':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'curam' and kw == 'tinggi' and ch == 'rendah':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'curam' and kw == 'tinggi' and ch == 'sedang':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'curam' and kw == 'tinggi' and ch == 'tinggi':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'sangat curam' and kw == 'rendah' and ch == 'rendah':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'sangat curam' and kw == 'rendah' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'sangat curam' and kw == 'rendah' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'sangat curam' and kw == 'rendah' and ch == 'rendah':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'sangat curam' and kw == 'rendah' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'sangat curam' and kw == 'rendah' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'tidak padat' and das == 'tinggi' and kl == 'sangat curam' and kw == 'tinggi' and ch == 'tinggi':
        result = 'aman'
    elif kp == 'tidak padat' and das == 'kecil' and kl == 'landai' and kw == 'rendah' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'kecil' and kl == 'landai' and kw == 'rendah' and ch == 'sedang':
        result = 'banjir'
    elif kp == 'padat' and das == 'kecil' and kl == 'landai' and kw == 'rendah' and ch == 'tinggi':
        result = 'banjir'
    elif kp == 'padat' and das == 'kecil' and kl == 'landai' and kw == 'sedang' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'kecil' and kl == 'landai' and kw == 'sedang' and ch == 'sedang':
        result = 'banjir'
    elif kp == 'padat' and das == 'kecil' and kl == 'landai' and kw == 'sedang' and ch == 'tinggi':
        result = 'banjir'
    elif kp == 'padat' and das == 'kecil' and kl == 'landai' and kw == 'tinggi' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'kecil' and kl == 'landai' and kw == 'tinggi' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'padat' and das == 'kecil' and kl == 'landai' and kw == 'tinggi' and ch == 'tinggi':
        result = 'banjir'
    elif kp == 'padat' and das == 'kecil' and kl == 'curam' and kw == 'rendah' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'kecil' and kl == 'curam' and kw == 'rendah' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'padat' and das == 'kecil' and kl == 'curam' and kw == 'rendah' and ch == 'tinggi':
        result = 'banjir'
    elif kp == 'padat' and das == 'kecil' and kl == 'curam' and kw == 'sedang' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'kecil' and kl == 'curam' and kw == 'sedang' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'padat' and das == 'kecil' and kl == 'curam' and kw == 'sedang' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'padat' and das == 'kecil' and kl == 'curam' and kw == 'tinggi' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'kecil' and kl == 'curam' and kw == 'tinggi' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'padat' and das == 'kecil' and kl == 'curam' and kw == 'tinggi' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'padat' and das == 'kecil' and kl == 'sangat curam' and kw == 'rendah' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'kecil' and kl == 'sangat curam' and kw == 'rendah' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'padat' and das == 'kecil' and kl == 'sangat curam' and kw == 'rendah' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'padat' and das == 'kecil' and kl == 'sangat curam' and kw == 'sedang' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'kecil' and kl == 'sangat curam' and kw == 'sedang' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'padat' and das == 'kecil' and kl == 'sangat curam' and kw == 'sedang' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'padat' and das == 'kecil' and kl == 'sangat curam' and kw == 'tinggi' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'kecil' and kl == 'sangat curam' and kw == 'tinggi' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'padat' and das == 'kecil' and kl == 'sangat curam' and kw == 'tinggi' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'landai' and kw == 'rendah' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'landai' and kw == 'rendah' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'landai' and kw == 'rendah' and ch == 'tinggi':
        result = 'banjir'
    elif kp == 'padat' and das == 'sedang' and kl == 'landai' and kw == 'sedang' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'landai' and kw == 'sedang' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'landai' and kw == 'sedang' and ch == 'tinggi':
        result = 'banjir'
    elif kp == 'padat' and das == 'sedang' and kl == 'landai' and kw == 'tinggi' and ch == 'rendah':
        result = 'aman'
    elif kp == 'padat' and das == 'sedang' and kl == 'landai' and kw == 'tinggi' and ch == 'sedang':
        result = 'aman'
    elif kp == 'padat' and das == 'sedang' and kl == 'landai' and kw == 'tinggi' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'curam' and kw == 'rendah' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'curam' and kw == 'rendah' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'curam' and kw == 'rendah' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'curam' and kw == 'sedang' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'curam' and kw == 'sedang' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'curam' and kw == 'sedang' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'curam' and kw == 'tinggi' and ch == 'rendah':
        result = 'aman'
    elif kp == 'padat' and das == 'sedang' and kl == 'curam' and kw == 'tinggi' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'curam' and kw == 'tinggi' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'sangat curam' and kw == 'rendah' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'sangat curam' and kw == 'rendah' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'sangat curam' and kw == 'rendah' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'sangat curam' and kw == 'sedang' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'sangat curam' and kw == 'sedang' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'sangat curam' and kw == 'sedang' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'sangat curam' and kw == 'tinggi' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'sangat curam' and kw == 'tinggi' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'padat' and das == 'sedang' and kl == 'sangat curam' and kw == 'tinggi' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'padat' and das == 'tinggi' and kl == 'landai' and kw == 'rendah' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'tinggi' and kl == 'landai' and kw == 'rendah' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'padat' and das == 'tinggi' and kl == 'landai' and kw == 'rendah' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'padat' and das == 'tinggi' and kl == 'landai' and kw == 'sedang' and ch == 'rendah':
        result = 'aman'
    elif kp == 'padat' and das == 'tinggi' and kl == 'landai' and kw == 'sedang' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'padat' and das == 'tinggi' and kl == 'landai' and kw == 'sedang' and ch == 'tinggi':
        result = 'banjir'
    elif kp == 'padat' and das == 'tinggi' and kl == 'landai' and kw == 'tinggi' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'tinggi' and kl == 'landai' and kw == 'tinggi' and ch == 'sedang':
        result = 'banjir'
    elif kp == 'padat' and das == 'tinggi' and kl == 'landai' and kw == 'tinggi' and ch == 'tinggi':
        result = 'banjir'
    elif kp == 'padat' and das == 'tinggi' and kl == 'curam' and kw == 'rendah' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'tinggi' and kl == 'curam' and kw == 'rendah' and ch == 'sedang':
        result = 'banjir'
    elif kp == 'padat' and das == 'tinggi' and kl == 'curam' and kw == 'rendah' and ch == 'tinggi':
        result = 'banjir'
    elif kp == 'padat' and das == 'tinggi' and kl == 'curam' and kw == 'sedang' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'tinggi' and kl == 'curam' and kw == 'sedang' and ch == 'sedang':
        result = 'banjir'
    elif kp == 'padat' and das == 'tinggi' and kl == 'curam' and kw == 'sedang' and ch == 'tinggi':
        result = 'banjir'
    elif kp == 'padat' and das == 'tinggi' and kl == 'curam' and kw == 'tinggi' and ch == 'rendah':
        result = 'aman'
    elif kp == 'padat' and das == 'tinggi' and kl == 'curam' and kw == 'tinggi' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'padat' and das == 'tinggi' and kl == 'curam' and kw == 'tinggi' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'padat' and das == 'tinggi' and kl == 'sangat curam' and kw == 'rendah' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'tinggi' and kl == 'sangat curam' and kw == 'rendah' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'padat' and das == 'tinggi' and kl == 'sangat curam' and kw == 'rendah' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'padat' and das == 'tinggi' and kl == 'sangat curam' and kw == 'sedang' and ch == 'rendah':
        result = 'rawan'
    elif kp == 'padat' and das == 'tinggi' and kl == 'sangat curam' and kw == 'sedang' and ch == 'sedang':
        result = 'rawan'
    elif kp == 'padat' and das == 'tinggi' and kl == 'sangat curam' and kw == 'sedang' and ch == 'tinggi':
        result = 'rawan'
    elif kp == 'padat' and das == 'tinggi' and kl == 'sangat curam' and kw == 'tinggi' and ch == 'tinggi':
        result = 'rawan'

    temp['result'] = result

    return temp

def getResult(kp, das, kl, kw, ch):
    kepadatan_penduduk = ''
    daerah_sungai = ''
    kemiringan_lereng = ''
    ketinggian_wilayah = ''
    curah_hujan = ''
    banjir = ''

    kp = int(kp)
    das = int(das)
    kl = int(kl)
    kw = int(kw)
    ch = int(ch)

#parameter kepadatan penduduk
    if kp >= 1 and kp <= 500:
        kepadatan_penduduk = 'tidak padat'

    elif kp > 500:
        kepadatan_penduduk = 'padat'

#parameter daerah aliran sungai
    if das >= 1 and das < 90000 :
        daerah_sungai = "kecil"
    elif das >= 90000 and das < 500000:
        daerah_sungai = "sedang"
    elif das > 500000 :
        daerah_sungai = "besar"

#parameter kemiringan lereng
    if kl >= 0 and kl <= 15 :
        kemiringan_lereng = "landai"
    elif kl >= 16 and kl <= 40 :
        kemiringan_lereng = "curam"
    elif kl > 40 :
        kemiringan_lereng = "sangat curam"

#parameter ketinggian wilayah
    if kw >= 1 and kw < 175 :
        ketinggian_wilayah = "rendah"
    elif kw >= 175 and kw <= 300 :
        ketinggian_wilayah = "sedang"
    elif kw > 300 :
        ketinggian_wilayah = "tinggi"

#parameter curah hujan
    if ch >= 1 and ch < 20 :
        curah_hujan = "rendah"
    elif ch >= 20 and ch <= 90 :
        curah_hujan = "sedang"
    elif ch > 90:
        curah_hujan = "tinggi"

    temp = {
        'kepadatan_penduduk':kepadatan_penduduk,
        'daerah_sungai': daerah_sungai,
        'kemiringan_lereng': kemiringan_lereng,
        'ketinggian_wilayah': ketinggian_wilayah,
        'curah_hujan': curah_hujan
    }

    return getConclusion(kepadatan_penduduk, daerah_sungai, kemiringan_lereng, ketinggian_wilayah, curah_hujan, temp)

if __name__ == '__main__':
    kp = int(input('Masukkan Kepadatan Penduduk: (jiwa/km2) '))
    das = int(input('Masukkan Daerah Aliran Sungai: (ha) '))
    kl = int(input("Masukkan Kemiringan Lereng: (%) "))
    kw = int(input("Masukkan Ketinggian Wilayah: (mdpl) "))
    ch = int(input("Masukkan Curah Hujan: (mm/hari) "))

    hasil = getResult(kp, das, kl, kw, ch)
    print(hasil)
    print("Prediksi : ", hasil['result'])