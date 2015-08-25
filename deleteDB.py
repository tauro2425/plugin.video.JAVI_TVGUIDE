
import os
import xbmc
import xbmcgui
import xbmcaddon

def deleteDB():
    try:
        xbmc.log("[script.tvguidemicro] Deleting database...", xbmc.LOGDEBUG)
        dbPath = xbmc.translatePath(xbmcaddon.Addon(id = 'script.tvguidemicro').getAddonInfo('profile'))
        dbPath = os.path.join(dbPath, 'source.db')

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
        d.ok('PLD TV Guide', '                        Base de datos eliminado correctamente')
    else:
        d = xbmcgui.Dialog()
        d.ok('PLD TV Guide', '                             Fallo L borrar Base de datos  ')
		
def deleteDB():
    try:
        xbmc.log("[script.tvguidemicro] Deleting Guide listing Choices...", xbmc.LOGDEBUG)
        dbPath = xbmc.translatePath(xbmcaddon.Addon(id = 'script.tvguidemicro').getAddonInfo('profile'))
        dbPath = os.path.join(dbPath, 'settings.xml')

        delete_file(dbPath)

        passed = not os.path.exists(dbPath)

        if passed:
            xbmc.log("[script.tvguidemicro] Deleting Guide listing Choices...PASSED", xbmc.LOGDEBUG)
        else:
            xbmc.log("[script.tvguidemicro] Deleting Guide listing Choices...FAILED", xbmc.LOGDEBUG)

        return passed

    except Exception, e:
        xbmc.log('[script.tvguidemicro] Deleting Guide listing Choices...EXCEPTION', xbmc.LOGDEBUG)
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
        d.ok('PLD TV Guide', 'PLD TV Guia Reseteado correctamente')
    else:
        d = xbmcgui.Dialog()
        d.ok('PLD TV Guide', 'Fallo al Resetear')

