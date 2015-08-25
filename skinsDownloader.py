
import xbmcgui
import os
import xbmc
import xbmcaddon
import download
import extract
import base64


def deleteDB():
    try:
        xbmc.log("[script.tvguidemicro] Deleting database...", xbmc.LOGDEBUG)
        dbPath = xbmc.translatePath(xbmcaddon.Addon(id = 'script.tvguidemicro').getAddonInfo('profile'))
        dbPath = os.path.join(dbPath, 'extras')

        delete_file(dbPath)
        
        passed = not os.path.exists(dbPath)

        if passed: 
            xbmc.log("[script.tvguidemicro] Deleting database...PASSED", xbmc.LOGDEBUG)
        else:
            xbmc.log("[script.tvguidemicro] Deleting database...FAILED", xbmc.LOGDEBUG)

        return passed

    except Exception, e:
        xbmc.log('[script.tvguidemicro] Deleting database...EXCEPTION', xbmc.LOGDEBUG)
        return False

def delete_file(filename):
    tries = 10
    while os.path.exists(filename) and tries > 0: 
        try:             
            os.remove(filename) 
            break 
        except: 
            tries -= 1 

if __name__ == '__main__':
    if deleteDB():
        d = xbmcgui.Dialog()
        d.ok('PLD TV Guide', '                        Extras eliminado correctamente')
    else:
        d = xbmcgui.Dialog()
        d.ok('PLD TV Guide', '                             DESEA DESCARGAR LOS SKINS  ')

ADDON  = xbmcaddon.Addon(id = 'script.tvguidemicro')
datapath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
extras   = os.path.join(datapath, 'extras')
skinfolder   = os.path.join(datapath, extras, 'skins')
dest     = os.path.join(extras, 'skins.zip')
url      = base64.b64decode('aHR0cDovL3BsZHR2Z3VpZGUucHJveWVjdG9sdXpkaWdpdGFsLmNvbS9wbGQtdHYtZ2lhL3NraW5zLXBhY2svc2tpbnMuemlw')


try:
    os.makedirs(skins)
    
except:
    pass

download.download(url, dest)
extract.all(dest, extras)

try:
    os.remove(dest)
except:
    pass
