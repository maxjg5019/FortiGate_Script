# 腳本需求

<aside>

    💡手動前置作業：拿掉 []、hxxp、http (留下純淨 FQDN)

</aside>

## 基礎功能

- 建立 IP 的 SubNet 物件
- 建立FQDN 的物件
- 新建 Address Group 物件 & 把剛建好的物件加進去
- 把剛建好的物件加到既有  Address Group 裡面 (用 append [參考](https://community.fortinet.com/t5/Support-Forum/How-to-append-an-address-to-an-address-group-without-replacing/m-p/204033))

## 防呆 & 一些命名規則

- IP 相關
    - Input 如果有 Port 號就在讀取時直接拿掉
    - set 時要加 /32
    - `set type subnet` (這通常不用 因為 FG 一開始預設 type 就是 subnet)
- FQDN 相關
    - 如果網址前面有 * 代表是 Wildcard，物件名稱前要加 `wildcard.`
    - set
- Address Group 相關
    - 新增物件(不會覆蓋既有物件)： append member `物件1 物件2`
    - 設定物件(覆蓋既有物件)：set  member `物件1 物件2`

## 工事進度

- [x]  用 Python 寫
- [ ]  長出 GUI 介面 可輸入 input、選擇功能並按照功能出現對應 input
- [ ]  input 資料清洗
- [ ]  儲存 input 並套用 CLI 指令格式 如何換行 or 如何 space
- [ ]  最後一筆要 end
- [ ]  整個文字產出成 txt

---

# 基礎 CLI 格式

```python
// 建 IP 物件
config firewall address
edit 118.107.47.75
set subnet 118.107.47.75/32
next
end

// 建 FQDN 物件
config firewall address
edit xxg.manarythubazar.com
set type fqdn
set fqdn xxg.manarythubazar.com
next

// 建 Address Gruop 
config firewall addrgrp
edit BlockList-DN
set member google.com yuotube.com
next
end

// 既有 Address Gruop 新增成員
config firewall addrgrp
edit BlockList-DN
append member reddit.com
end
```

---

- `地基主 (賽博乖乖 & 活人獻祭)`
    
    <aside>
      
      💡天靈靈地靈靈，所有功能都順利，我不想再值夜班ㄌ。
  
    </aside>
    
    ```
                                   `-+syhddmmmddhyo+:`                              
                                .+hmmdddddddddddddddmmds/`      ``...`              
                             `/hmddddddddddddddddddddddddmy++osyhyyyhhs.            
                           `ommddddddddddddddddddddddddddddmmdys+++syhhh:           
               .`         /mmddddddddddddddddddddddddddddddddmmhyyyyyyyyh/          
           `:sdNy`      .ymddddddddddddddddddddddddddddddddddddmdhhhyyyyyh-         
       `.+hmmmddmo     -mmddddddddddddddddddddddddddddddddddddddmmhhhhhhhh+         
      odmmdddddddms` `+mmddddddddddddddddddddddddddddddddddddddddmmddhhhhh+         
      ymdmmmmmmmmdmmdmmdddddddddddddmmddddddddddddddddddddddddddddmd:ydhhd:         
      :Nmmmmmmmmmmmmmmddy+::+ydddms/:::/+osydmdddddddddddddddddddddN-`:+o:          
       ymmmmmmmmmmmmmmdo.`.``/hmm/+hdd/``````-+ydmdddddddddddddddddmy               
       .mmmmmmmmmmmmmmh:`-o+`:hm/`-o:.```````os/./ymddddddddddddddddN`              
        /Nmmmmmmmmmmmmh:..::-od/``dMs````````/hNm:`-ymddddddddddddddN-              
         sNmmmmmmmmmmmd+-:/-.`..`.hh:`...``:hh..:```:NdmmmmmmmdmddddN/              
      `::/dmmmmmmmmmmmmdo:```./d/````-..:`-mdd.````.dmdmmmmmmmmmmmdmmy              
    ./::-..+dmmmmmmmmmmh/````-dNms-```..``.+/`````-dmds/:-:ohmmmmmmmmN.             
    -/.``--`/dmmmdysydmy.````omNd+.-::-...-:os:..`-hs-``.``./hmmmmmmmmd.       .os` 
    /:---.`.`-/sy:```omy-````hddo` `s.``/NNNNo...`````-+o/``/dmmmmmmmmmms:..:+ymmN: 
    :/.``.``````-``./dNh/````syyyhshd-``:mNmy.````````.```./hmmmmmmmmmmmmmmmmmmmmmd 
     .::-```...````+dNNNs-```//::/+ooosyhdds.``````-----:+ydmmmmmmmmmmmmmmmmmmmmmmN:
       `:/````..``-shhdmms-``./::/:::::::+/``````.+dmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmd
         ./:-```.-oyyhyhhhy+.`.:/::::///:.````..:ymNNmmo:/ymmmmmmmmmmmmmmmmmmmmmmmmN
           `:y:./yyyyyyyyhh///:..--:--.````..-/ymNNNNNy.``-hNNNNNmmmmmmmmmmmmmmNmh+-
           `ymdyhyyyyyyhhy/---o+///:::::://oyhmNNNNNNNo```:osyho/---:ymmNNNNmho:`   
           `+hhhhhyyyyhhs-----y--o/------:+hhhhhhhddds.````````..-..-+dNds+-`       
             `.:+oossyyyy:---:ssoy:------+hyyyyhhyyys-``....```..--..//`            
                        syysyysssho:-----ohyyyyhyhhyy/`````..``````-o.              
                       `hssssssoyhhyo+++syyhhhhyyhyyh+:::-..-:::::::.               
                       :hysssyo/yhhssyysssssyhyhhhyhdmmy....`                       
                       shyyyyyyhhhhyyyyyyyyyyhh/-+syhdo`                            
                      `hhhhhhhhhhhhhhhhhhhhhhhhy`                                   
                       -:yhyyyysyhhyyyyyyyyyyyyh-                                   
                         -hysssssyydsyyssssssssyh.                                  
                          /hsysyyyyd-.+yyyssyyssyh-                                 
              -/+oo++/-`   +hhyhhhso`  .ohyyyyyyhho:`   `-:/++++/:.                 
           -+ooooooooooso+/ssss.yy:      `//+ds/oysss+ossoooooooo+os/.              
        `:o+:/oooooooooooooooossyh:          oyyssooooooooooooooo+/:os+`            
       -ssoooooooooooooooooosssssy+          .hyssssssooooooooooooooooss-           
       /syysssssssssssssssyyyyyyyh-           shyyyysyyysssssssssssssssyy           
         `-/+ossyyyysso+/:-./++//.             .---` `.-:/+oossssoo++/:-`           
    ```
