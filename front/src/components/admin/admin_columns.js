import building from '../../assets/building.png'

const center_columns = [
    { field: 'id', headerName: 'ID', width: 50 },
    { field: 'image', headerName: 'Image', width: 70,
      renderCell: (params) => {
          if (params.row.photo == null){
            return (
              <p>
                <img src={building} className='admin-table-image'/>
              </p>
            )
          } else {
            return(
              <img src={params.row.photo} className='admin-table-image'/>
            )
          }
          
      }
    },
    { field: 'title', headerName: 'Title', width: 200 },
    { field: 'address', headerName: 'Address', width: 200 },
    {
      field: 'region',
      headerName: 'Region',
      width: 200,
    },
    {
      field: 'website',
      headerName: 'Website',
      width: 200,
    },
    {
      field: 'tags',
      headerName: 'Tags',
      description: 'This column has a value getter and is not sortable.',
      sortable: false,
      width: 20,
      valueGetter: (params) =>
        `${params.row.tags.length || ''}`,
    },
  ];

export default { center_columns };