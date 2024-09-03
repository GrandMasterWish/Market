import streamlit as st
import pandas as pd
import ccxt
import plotly.express as px

# Initialize exchange (Binance)
exchange = ccxt.bitget()

# Function to fetch OHLCV data and calculate pivot points
def calculate_pivot(symbol, timeframe):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=2)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    
    # Calculate high, low, and close of the previous period
    previous_period = df.iloc[-2]
    high = previous_period['high']
    low = previous_period['low']
    close = previous_period['close']
    
    # Calculate pivot points
    pivot = (high + low + close) / 3
    
    # Get current price
    ticker = exchange.fetch_ticker(symbol)
    current_price = ticker['last']
    
    # Determine above or below pivot
    status = 'Above Pivot' if current_price > pivot else 'Below Pivot'
    
    return {
        'symbol': symbol,
        'current_price': current_price,
        'pivot': pivot,
        'status': status
    }

# Function to generate trading data for a list of symbols
def generate_trading_data(symbol_list, timeframe):
    data = []
    for symbol in symbol_list:
        try:
            data.append(calculate_pivot(symbol, timeframe))
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
    return data

# List of symbols to analyze
symbol_list = [
    "10000WEN/USDT", "1000APU/USDT", "1000BONK/USDT", "1000RATS/USDT", "1CAT/USDT", 
        "1INCH/USDT", "A8/USDT", "AAVE/USDT", "ACH/USDT", "ACE/USDT", "ADA/USDT", 
        "AEVO/USDT", "AGLD/USDT", "AI/USDT", "AIOZ/USDT", "AKRO/USDT", "ALGO/USDT", 
        "ALICE/USDT", "ALPHA/USDT", "ALT/USDT", "AMB/USDT", "AMP/USDT", "API3/USDT", 
        "APE/USDT", "APT/USDT", "ARB/USDT", "AR/USDT", "ARPA/USDT", "ARKM/USDT", 
        "ARK/USDT", "ATH/USDT", "ATOM/USDT", "AUCTION/USDT", "AUDIO/USDT", 
        "AVAIL/USDT", "AVAX/USDT", "AXS/USDT", "BAKE/USDT", "BANANA/USDT", "BAND/USDT", 
        "BANDOG/USDT", "BB/USDT", "BCH/USDT", "BEAMX/USDT", "BEL/USDT", "BENDOG/USDT", 
        "BETA/USDT", "BIGTIME/USDT", "BICO/USDT", "BIFI/USDT", "BLAST/USDT", "BLUR/USDT", 
        "BLZ/USDT", "BNB/USDT", "BNXNEW/USDT", "BOME/USDT", "BONE/USDT", "BOND/USDT", 
        "BRETT/USDT", "BSV/USDT", "BTC/USDT", "BTT/USDT", "BURGER/USDT", "BZZ/USDT", 
        "CADE/USDT", "CAKE/USDT", "CELO/USDT", "CFX/USDT", "CHAOS/USDT", "CHZ/USDT", 
        "CKB/USDT", "CLV/USDT", "CMOVIE/USDT", "CRO/USDT", "CRV/USDT", "CTK/USDT", 
        "CTSI/USDT", "CTXC/USDT", "CVC/USDT", "C98/USDT", "DAR/USDT", "DARK/USDT", 
        "DASH/USDT", "DATA/USDT", "DEGO/USDT", "DENT/USDT", "DEP/USDT", "DERO/USDT", 
        "DFA/USDT", "DGB/USDT", "DIFX/USDT", "DODO/USDT", "DOGE/USDT", "DOME/USDT", 
        "DONE/USDT", "DOSE/USDT", "DOWS/USDT", "DPX/USDT", "DREAMS/USDT", "DSLA/USDT", 
        "DYDX/USDT", "EDEN/USDT", "EFI/USDT", "EGAME/USDT", "ELA/USDT", "ELF/USDT", 
        "ELT/USDT", "ENJ/USDT", "ENS/USDT", "EPIK/USDT", "EPK/USDT", "ERN/USDT", 
        "ETC/USDT", "ETH/USDT", "ETHW/USDT", "EUROC/USDT", "FAME/USDT", "FARM/USDT", 
        "FET/USDT", "FIL/USDT", "FINE/USDT", "FLOKI/USDT", "FLOW/USDT", "FLR/USDT", 
        "FLUX/USDT", "FNCY/USDT", "FODL/USDT", "FRONT/USDT", "FRR/USDT", "FTM/USDT", 
        "FTT/USDT", "FUN/USDT", "FUSE/USDT", "FXS/USDT", "GALA/USDT", "GBYTE/USDT", 
        "GGT/USDT", "GLOW/USDT", "GMX/USDT", "GNO/USDT", "GODS/USDT", "GOFX/USDT", 
        "GOG/USDT", "GOM2/USDT", "GRT/USDT", "GTC/USDT", "GXC/USDT", "HACK/USDT", 
        "HARD/USDT", "HFT/USDT", "HIT/USDT", "HNT/USDT", "HOT/USDT", "ICP/USDT", 
        "ILV/USDT", "IMX/USDT", "INJ/USDT", "INSUR/USDT", "IOTA/USDT", "IQ/USDT", 
        "IRIS/USDT", "JASMY/USDT", "JUNO/USDT", "KAF/USDT", "KAVA/USDT", "KDA/USDT", 
        "KEEP/USDT", "KILT/USDT", "KLAY/USDT", "KLV/USDT", "KP3R/USDT", "KSM/USDT", 
        "LAI/USDT", "LATTE/USDT", "LAZIO/USDT", "LCX/USDT", "LDO/USDT", "LEG/USDT", 
        "LEGO/USDT", "LEND/USDT", "LINA/USDT", "LINK/USDT", "LIT/USDT", "LITH/USDT", 
        "LOOKS/USDT", "LOOM/USDT", "LRC/USDT", "LSK/USDT", "LTC/USDT", "LTO/USDT", 
        "MAGIC/USDT", "MANA/USDT", "MASK/USDT", "MCB/USDT", "MCRN/USDT", "MDT/USDT", 
        "MEDIA/USDT", "MEGA/USDT", "MER/USDT", "MESA/USDT", "MFT/USDT", "MFTU/USDT", 
        "MGB/USDT", "MHB/USDT", "MINA/USDT", "MKR/USDT", "MLT/USDT", "MMPRO/USDT", 
        "MOVD/USDT", "MOVR/USDT", "MTL/USDT", "MXC/USDT", "MX/USDT", "NARUTO/USDT", 
        "NAVI/USDT", "NEAR/USDT", "NEO/USDT", "NFT/USDT", "NFTD/USDT", "NKN/USDT", 
        "NMR/USDT", "NOIA/USDT", "NULS/USDT", "NVT/USDT", "OAX/USDT", "OCEAN/USDT", 
        "OG/USDT", "OMG/USDT", "ONE/USDT", "OOE/USDT", "OOKI/USDT", "OP/USDT", 
        "ORC/USDT", "ORDI/USDT", "ORN/USDT", "OSMO/USDT", "PENDLE/USDT", "PEOPLE/USDT", 
        "PERSIST/USDT", "PIVX/USDT", "PLA/USDT", "PLAY/USDT", "PLY/USDT", "POLS/USDT", 
        "POLYX/USDT", "POOLX/USDT", "PORTO/USDT", "POWR/USDT", "PROS/USDT", "PUNDIX/USDT", 
        "PYR/USDT", "QI/USDT", "QNT/USDT", "QRDO/USDT", "QUICK/USDT", "RACA/USDT", 
        "RAMP/USDT", "RARI/USDT", "RAZOR/USDT", "RDNT/USDT", "REAL/USDT", "REEF/USDT", 
        "REKT/USDT", "REN/USDT", "REQ/USDT", "REVO/USDT", "RIF/USDT", "RNDR/USDT", 
        "ROGUE/USDT", "RSR/USDT", "RSS3/USDT", "SAND/USDT", "SANTOS/USDT", "SAR/USDT", 
        "SBDO/USDT", "SBT/USDT", "SC/USDT", "SDAO/USDT", "SDN/USDT", "SHIBA/USDT", 
        "SHIB/USDT", "SHILL/USDT", "SHIT/USDT", "SHROOMS/USDT", "SKL/USDT", "SLS/USDT", 
        "SLV/USDT", "SNT/USDT", "SNY/USDT", "SOL/USDT", "SOS/USDT", "SPELL/USDT", 
        "SPS/USDT", "SRM/USDT", "STEP/USDT", "STG/USDT", "STMX/USDT", "STRK/USDT", 
        "STRM/USDT", "STX/USDT", "SUI/USDT", "SUPER/USDT", "SUSHI/USDT", "SWEAT/USDT", 
        "SWFTC/USDT", "SXP/USDT", "SYN/USDT", "T/USDT", "TAMA/USDT", "TAP/USDT", 
        "TCR/USDT", "TCT/USDT", "TGBP/USDT", "TLOS/USDT", "TON/USDT", "TORN/USDT", 
        "TOWER/USDT", "TPL/USDT", "TRA/USDT", "TRIBE/USDT", "TRX/USDT", "TRYB/USDT", 
        "TULIP/USDT", "TWT/USDT", "TVK/USDT", "TWT/USDT", "UBX/USDT", "UMA/USDT", 
        "UMEE/USDT", "UNCX/USDT", "UNFI/USDT", "UNI/USDT", "USDT/USDT", "VET/USDT", 
        "VGX/USDT", "VIB/USDT", "VITE/USDT", "VRA/USDT", "VRSC/USDT", "VXV/USDT", 
        "WAN/USDT", "WAVES/USDT", "WBTC/USDT", "WEMIX/USDT", "WILD/USDT", "WIN/USDT", 
        "WNCG/USDT", "XCAD/USDT", "XEM/USDT", "XETA/USDT", "XLM/USDT", "XMR/USDT", 
        "XNO/USDT", "XRP/USDT", "XTAG/USDT", "XTZ/USDT", "YGG/USDT", "ZBC/USDT", 
        "ZEC/USDT", "ZEN/USDT", "ZIL/USDT", "ZKS/USDT", "ZRX/USDT"

]

# Main Streamlit app
st.title('Cryptocurrency Pivot Point Analysis')

# Get trading data for daily, weekly, and monthly pivots
daily_data = generate_trading_data(symbol_list, '1d')
weekly_data = generate_trading_data(symbol_list, '1w')
monthly_data = generate_trading_data(symbol_list, '1M')

# Function to create pie charts for pivot statuses
def create_pie_chart(data, title):
    df = pd.DataFrame(data)
    above_pivot_count = df[df['status'] == 'Above Pivot'].shape[0]
    below_pivot_count = df[df['status'] == 'Below Pivot'].shape[0]
    
    pie_data = pd.DataFrame({
        'Status': ['Above Pivot', 'Below Pivot'],
        'Count': [above_pivot_count, below_pivot_count]
    })
    
    fig = px.pie(pie_data, values='Count', names='Status', title=title)
    return fig

# Display data and pie charts
if daily_data and weekly_data and monthly_data:
    st.header('Daily Pivots')
    st.dataframe(pd.DataFrame(daily_data))
    st.plotly_chart(create_pie_chart(daily_data, 'Symbols Above and Below Daily Pivot'))

    st.header('Weekly Pivots')
    st.dataframe(pd.DataFrame(weekly_data))
    st.plotly_chart(create_pie_chart(weekly_data, 'Symbols Above and Below Weekly Pivot'))

    st.header('Monthly Pivots')
    st.dataframe(pd.DataFrame(monthly_data))
    st.plotly_chart(create_pie_chart(monthly_data, 'Symbols Above and Below Monthly Pivot'))

    # Market sentiment based on combined pivot status
    overall_status = []
    for daily, weekly, monthly in zip(daily_data, weekly_data, monthly_data):
        if daily['status'] == 'Above Pivot' and weekly['status'] == 'Above Pivot' and monthly['status'] == 'Above Pivot':
            overall_status.append('Bullish')
        elif daily['status'] == 'Below Pivot' and weekly['status'] == 'Below Pivot' and monthly['status'] == 'Below Pivot':
            overall_status.append('Bearish')
        else:
            overall_status.append('Neutral')
    
    market_sentiment_data = pd.DataFrame({
        'Symbol': [d['symbol'] for d in daily_data],
        'Market Sentiment': overall_status
    })
    
    sentiment_counts = market_sentiment_data['Market Sentiment'].value_counts()
    
    sentiment_pie_data = pd.DataFrame({
        'Sentiment': sentiment_counts.index,
        'Count': sentiment_counts.values
    })
    
    st.header('Overall Market Sentiment')
    st.plotly_chart(px.pie(sentiment_pie_data, values='Count', names='Sentiment', title='Market Sentiment Based on Daily, Weekly, and Monthly Pivots'))
else:
    st.warning("No data available.")


