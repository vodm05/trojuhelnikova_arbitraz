# trojuhelnikova_arbitraz
Trading bot pracující s myšlenkou trojuhleníkové arbitráže na platformě mexc

Kód pracuje s myšlenkou směn ze základní měny, kterou je "USDC". Z této měny se převede do "BTC" a následně do další měny, např. ADA či SOL. Poslední směnou se vrací zpět do USDC.

Byla vybrána měna USDC, jejíž kurz je téměř srovnatelný s USD. Tím by se mělo zabránit volatilitě na krypto burze, která by mohla značně ovlivnit ziskovost v případě zvolení klasické krypto měny, např. BTC.

Nedostatkem na této platformě je nemožnost využití market orderu, který by okmažitě provedl směnu.
