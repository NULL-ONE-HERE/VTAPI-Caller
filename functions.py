import vt

def vt_intergration():
    """Integration with VirusTotal"""
    with vt.Client('<token>') as client:
        try:
            file = client.get_object('/files/{}', '9f184843fc180982b9ce89a40a5f6118')
            print(file.last_analysis_stats)
            client.close()
        except vt.APIError as e:
            print(e)
            client.close()

if __name__ == '__main__':
    vt_intergration()