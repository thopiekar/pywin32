// This file declares the IContextMenu Interface and Gateway for Python.
// Generated by makegw.py
// ---------------------------------------------------
// ---------------------------------------------------
//
// Gateway Declaration
#pragma once

#include "PyIContextMenu.h"

class PyGContextMenu2 : public PyGContextMenu, public IContextMenu2 {
   protected:
    PyGContextMenu2(PyObject *instance) : PyGContextMenu(instance) { ; }
    PYGATEWAY_MAKE_SUPPORT2(PyGContextMenu2, IContextMenu2, IID_IContextMenu2, PyGContextMenu)

    // IContextMenu
    STDMETHOD(QueryContextMenu)(HMENU hmenu, UINT indexMenu, UINT idCmdFirst, UINT idCmdLast, UINT uFlags);

    STDMETHOD(InvokeCommand)(CMINVOKECOMMANDINFO __RPC_FAR *lpici);

    STDMETHOD(GetCommandString)(UINT_PTR idCmd, UINT uType, UINT __RPC_FAR *pwReserved, LPSTR pszName, UINT cchMax);
    // IContextMenu2
    STDMETHOD(HandleMenuMsg)(UINT uMsg, WPARAM wParam, LPARAM lParam);
};
