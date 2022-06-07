def getConclusion(kp, das, kl, kw, ch):
    result = ''

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

    print("Prediksi : ", result)

def getResult(kp, das, kl, kw, ch):
    kepadatan_penduduk = ''
    daerah_sungai = ''
    kemirendah_lereng = ''
    ketinggian_wilayah = ''
    curah_hujan = ''

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

#parameter kemirendah lereng
    if kl >= 0 and kl <= 15 :
        kemirendah_lereng = "landai"
    elif kl >= 16 and kl <= 40 :
        kemirendah_lereng = "curam"
    elif kl > 40 :
        kemirendah_lereng = "sangat curam"

#parameter ketinggian wilayah
    if kw < 175 :
        ketinggian_wilayah = "rendah"
    elif kw >= 175 and kw <= 300 :
        ketinggian_wilayah = "sedang"
    elif kw > 300 :
        ketinggian_wilayah = "tinggi"

#parameter curah hujan
    if ch < 20 :
        curah_hujan = "rendah"
    elif ch >= 20 and ch <= 90 :
        curah_hujan = "sedang"
    elif ch > 90:
        curah_hujan = "tinggi"

    temp = {
        'kepadatan_penduduk':kepadatan_penduduk,
        'daerah_sungai': daerah_sungai,
        'kemirendah_lereng': kemirendah_lereng,
        'ketinggian_wilayah': ketinggian_wilayah,
        'curah_hujan': curah_hujan
    }

    print(temp)
    getConclusion(kepadatan_penduduk, daerah_sungai, kemirendah_lereng, ketinggian_wilayah, curah_hujan)

if __name__ == '__main__':
    kp = int(input('Masukkan Kepadatan Penduduk (jiwa/km2) : '))
    das = int(input('Masukkan Daerah Aliran Sungai (ha) : '))
    kl = int(input("Masukkan Kemirendah Lereng (%) : "))
    kw = int(input("Masukkan Ketinggian Wilayah (mdpl) : "))
    ch = int(input("Masukkan Curah Hujan (mm/hari) : "))
    getResult(kp, das, kl, kw, ch)

    # test case 1
    # elif kp == 'padat' and das == 'sedang' and kl == 'landai' and kw == 'sedang' and ch == 'tinggi':
    #     result = 'banjir'

    # test case 2
    #     if kp == 'tidak padat' and das == 'kecil' and kl == 'landai' and kw == 'rendah' and ch == 'rendah':
    #         result = 'rawan'

    # elif kp == 'padat' and das == 'sedang' and kl == 'landai' and kw == 'tinggi' and ch == 'rendah':
    #     result = 'aman'

